#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pandas as pd
import os, django
import numpy as np
from collections import defaultdict
import operator
import jieba
import jieba.analyse
from sklearn.decomposition import PCA

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backGround.settings")
django.setup()

from articles.models import Article
from user_operations.models import UserReadAricle
rec_num = 6


class IDFLoader(object):
    def __init__(self, idf_path):
        self.idf_path = idf_path
        self.idf_freq = {}  # idf
        self.mean_idf = 0.0  # 均值
        self.load_idf()

    def load_idf(self):  # 从文件中载入idf
        cnt = 0
        with open(self.idf_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    word, freq = line.strip().split(' ')
                    cnt += 1
                except Exception as e:
                    pass
                self.idf_freq[word] = float(freq)

        print('Vocabularies loaded: %d' % cnt)
        self.mean_idf = sum(self.idf_freq.values()) / cnt


class TFIDF(object):
    def __init__(self, idf_path):
        self.idf_loader = IDFLoader(idf_path)
        self.idf_freq = self.idf_loader.idf_freq
        self.mean_idf = self.idf_loader.mean_idf

    def stopwordslist(self):
        stopwords = [line.strip() for line in open(r'F:\Projects\ClassDesign\backGround\apps\utils\algorithm\stopwords.txt', encoding='UTF-8').readlines()]
        return stopwords

    # 对句子进行中文分词
    def seg_depart(self, sentence):
        # 对文档中的每一行进行中文分词
        # print("正在分词")
        sentence_depart = jieba.cut("".join(sentence.split()), HMM=True)
        # 创建一个停用词列表
        stopwords = self.stopwordslist()
        # 输出结果为words
        words = []
        # 去停用词
        for word in sentence_depart:
            if word not in stopwords:
                if word != '\t':
                    words.append(word)
        return words

    def feature_select(self, list_words):
        # 总词频统计
        doc_frequency = defaultdict(int)
        for i in list_words:
            doc_frequency[i] += 1

        # 计算每个词的TF值
        word_tf = {}  # 存储每个词的tf值
        for i in doc_frequency:
            word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())

        # 计算每个词的IDF值
        word_idf = {}  # 存储每个词的idf值
        for i in doc_frequency:
            try:
                word_idf[i] = self.idf_freq[i]
            except Exception as e:
                word_idf[i] = -1
                # print(e)
                continue

        # 计算每个词的TF*IDF的值
        word_tf_idf = {}
        for i in doc_frequency:
            word_tf_idf[i] = word_tf[i] * word_idf[i]

        # 对字典按值由大到小排序
        dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
        df = dict_feature_select
        return df


class DataProcessing(object):
    feature = {}
    last_recommend = []

    def __init__(self):
        self.feature = self.get_feature_matrix()

    def random_int_list(self, start, stop, length):
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        length = int(abs(length)) if length else 0
        random_list = []
        for i in range(length):
            random_list.append(random.randint(start, stop))
        return random_list

    def cos_sim(self, vector_a, vector_b):
        vector_a = np.mat(vector_a)
        vector_b = np.mat(vector_b)
        num = float(vector_a * vector_b.T)
        denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
        cos = num / denom
        return cos

    def get_feature_matrix(self):
        tf = TFIDF(r'F:\Projects\ClassDesign\backGround\apps\utils\algorithm\idf.txt')
        articles = Article.objects.all()
        articles_df = pd.DataFrame(articles.values('id', 'content', 'typ'))
        id_list = articles_df['id']
        text_list = articles_df['content']
        words_list = []
        for i in text_list:
            words_list.append(tf.seg_depart(i))
        tf_idf_dic = {}
        for i in range(0, len(id_list)):
            id = id_list[i]
            tf_idf_dic.setdefault(id, {})
            for j in tf.feature_select(words_list[i]):
                tf_idf_dic[id].setdefault(j[0], j[1])
        tf_idf_df = pd.DataFrame(tf_idf_dic)
        tf_idf_df.fillna(0, inplace=True)
        return {col: tf_idf_df[col].tolist() for col in tf_idf_df.columns}

    def cosin_distance(self, user_id):
        read_article_queryset = UserReadAricle.objects.filter(user=user_id).values()
        try:
            articles = pd.DataFrame(read_article_queryset)['article_id']
            lis = []
            articles1 = []
            for i in articles:
                articles1.append(i)
            for i in articles:
                for j in range(0, len(self.feature[i])):
                    lis.append(0.0)
                break
            user_feature = np.array(lis)
            for i in articles:
                if i in self.last_recommend:
                    continue
                user_feature += np.array(self.feature[i])
            x = user_feature / articles.size
            sim_grade = {}
            for key, value in self.feature.items():
                sim_grade.setdefault(key, self.cos_sim(x, value))
            order_sim_grade = sorted(sim_grade.items(), key=operator.itemgetter(1), reverse=True)
            recommend_list = []
            for i in order_sim_grade:
                recommend_list.append(i[0])
            self.last_recommend = recommend_list[:rec_num]
            random.shuffle(self.last_recommend)
            return self.last_recommend
        except:
            l = Article.objects.count()
            l1 = 15
            random_list = self.random_int_list(59, 59 + l, l1)
            return random_list


if __name__ == '__main__':
    d = DataProcessing()
    print(d.cosin_distance('17'))


