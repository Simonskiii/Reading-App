# userCF
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

sim_num = 100
rec_num = 20


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


class UserCF(object):
    last_recommend = []
    dataset = {}
    article_user = {}

    def data_processing(self):
        read_article_queryset = UserReadAricle.objects.all()
        read_record = pd.DataFrame(read_article_queryset.values('user', 'article'))
        # 用户阅读文章字典
        for row in read_record.itertuples(index=True, name='Pandas'):
            admin = getattr(row, "user")
            article = getattr(row, "article")
            self.dataset.setdefault(admin, {})
            self.dataset[admin].setdefault(article, 0)
            self.dataset[admin][article] += 1

        for user, articles in self.dataset.items():
            for article in articles:
                if article not in self.article_user:
                    self.article_user[article] = set()
                self.article_user[article].add(user)
        # 同时阅读两篇文章的人数
        for article, users in self.article_user.items():
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    cf_sim_matrix.setdefault(u, {})
                    cf_sim_matrix[u].setdefault(v, 0)
                    cf_sim_matrix[u][v] += 1

        for u, related_users in cf_sim_matrix.items():
            for i, count in related_users.items():
                cf_sim_matrix[u][i] = count / math.sqrt(len(self.dataset[u]) * len(self.dataset[i]))
        for u, i in cf_sim_matrix.items():
            cf_sim_matrix.update({u: sorted(i.items(), key=itemgetter(1), reverse=True)})

    def recommend_list(self, user):
        read_record_queryset = UserReadAricle.objects.filter(user=user)
        try:
            read_record = pd.DataFrame(read_record_queryset.values('article'))['article'].unique()
            rank = {}
            for v, wuv in cf_sim_matrix[user]:
                try:
                    for article in self.dataset[v]:
                        if article in read_record:
                            continue
                        if article in self.last_recommend:
                            continue
                        rank.setdefault(article, 0)
                        rank[article] += wuv
                except:
                    continue
            rank = sorted(rank.items(), key=itemgetter(1), reverse=True)[:rec_num]
            lis = [x[0] for x in rank]
            # 推荐出来的数组长度
            first_lengh = len(lis)
            if first_lengh < rec_num:
                extra_articles = Article.objects.exclude(id__in=lis).values('id')
                extra_articles_list = list(extra_articles)
                l = len(extra_articles_list)
                # 推荐出来的数量和需要的数量之差
                second_length = rec_num - first_lengh
                extra_lis = random_int_list(1, l, second_length if second_length < l else l)
                for i in extra_lis:
                    lis.append(extra_articles_list[i - 1]['id'])
            self.last_recommend = lis
            random.shuffle(lis)
            return lis
        except:
            l = Article.objects.count()
            l1 = 15
            random_list = random_int_list(59, 59 + l, l1)
            return random_list


if __name__ == '__main__':
    usercf = UserCF()
    usercf.data_processing()
    print(usercf.recommend_list(17))
    print(usercf.recommend_list(17))
    print(usercf.recommend_list(17))
