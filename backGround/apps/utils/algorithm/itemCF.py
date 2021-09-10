# itemCF
import random

import pandas as pd
import math
from operator import itemgetter
import os, django

from django.forms import model_to_dict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backGround.settings")
django.setup()
from user_operations.models import UserReadAricle
from articles.models import Article
from backGround.settings import cf_sim_matrix


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    if stop - start + 1 == length:
        return range(1, length)
    for i in range(length):
        while True:
            value = random.randint(start, stop)
            if value not in random_list:
                random_list.append(value)
                break
    return random_list


class ItemCf(object):
    last_recommend = []
    rec_num = 20
    dataset = {}
    item_read_times = {}
    def data_processing(self):
        read_article_queryset = UserReadAricle.objects.all()
        read_record = pd.DataFrame(read_article_queryset.values('user', 'article'))
        # 用户阅读文章字典
        for row in read_record.itertuples(index=True, name='Pandas'):
            user = getattr(row, "user")
            self.dataset.setdefault(user, {})
            self.dataset[user][getattr(row, "article")] = 1

        for user, items in self.dataset.items():
            for item in items:
                if item not in self.item_read_times:
                    self.item_read_times[item] = 0
                self.item_read_times[item] += 1
        # 同时阅读两篇文章的人数
        for user, items in self.dataset.items():
            for i1 in items:
                for i2 in items:
                    if i1 == i2:
                        continue
                    cf_sim_matrix.setdefault(i1, {})
                    cf_sim_matrix[i1].setdefault(i2, 0)
                    cf_sim_matrix[i1][i2] += 1
        print("文章矩阵已完毕")

        for u, related_articles in cf_sim_matrix.items():
            for i, count in related_articles.items():
                if self.item_read_times[u] == 0 or self.item_read_times[i] == 0:
                    cf_sim_matrix[u][i] = 0
                else:
                    cf_sim_matrix[u][i] = count / math.sqrt(self.item_read_times[u] * self.item_read_times[i])
        for u, i in cf_sim_matrix.items():
            cf_sim_matrix.update({u: sorted(i.items(), key=itemgetter(1), reverse=True)})
        print(read_record)
        print("文章相似度矩阵完毕")



    def recommend_list(self, user):
        read_record_queryset = UserReadAricle.objects.filter(user=user)
        try:
            read_record = pd.DataFrame(read_record_queryset.values('article'))['article'].unique()
            rank = {}
            for article in read_record:
                try:
                    for related_article, w in cf_sim_matrix[article]:
                        try:
                            if related_article in read_record:
                                continue
                            if related_article in self.last_recommend:
                                continue
                            rank.setdefault(related_article, 0)
                            rank[related_article] += w
                        except:
                            continue
                except:
                    continue
            rank = sorted(rank.items(), key=itemgetter(1), reverse=True)[:self.rec_num]
            lis = [x[0] for x in rank]
            # 推荐出来的数组长度
            first_lengh = len(lis)
            if first_lengh < self.rec_num:
                extra_articles = Article.objects.exclude(id__in=lis).values('id')
                extra_articles_list = list(extra_articles)
                l = len(extra_articles_list)
                # 推荐出来的数量和需要的数量之差
                second_length = self.rec_num - first_lengh
                # if start <= stop else (int(stop), int(start)

                extra_lis = random_int_list(1, l, second_length if second_length < l else l)
                for i in extra_lis:
                    lis.append(extra_articles_list[i - 1]['id'])
            random.shuffle(lis)
            self.last_recommend = lis
            return lis
        except:
            l = Article.objects.count()
            l1 = 15
            random_list = random_int_list(59, 59 + l, l1)
            return random_list




