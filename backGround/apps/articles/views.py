import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from articles.filter import ArticleFilter
from backGround.settings import data_processing, itemcf
from user_operations.models import UserReadAricle, Comment
from user_operations.serializers import CommentSerializer
from utils.baseResponse import baseResponse, articleResponse
from .models import Article
from rest_framework import status, permissions, filters
from .serializers import AritcleShowSerializer, AriticleCreateSerializer, AritcleRetrieveSerializer


# Create your views here.


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


class ArticleTypeViewSet(GenericViewSet, ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = AritcleShowSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    filter_class = ArticleFilter

    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('typ',)


class ArticleViewset(CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Article.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return AritcleShowSerializer
        elif self.action == 'create':
            return AriticleCreateSerializer
        else:
            return AritcleRetrieveSerializer

    def list(self, request, *args, **kwargs):
        # lis = data_processing.cosin_distance(request.user.id)
        # 协同过滤
        lis = itemcf.recommend_list(self.request.user)
        article_ = Article.objects.filter(id__in=lis)
        articles = AritcleShowSerializer(article_, many=True)

        # following = [1, 2, 3]
        # publish_list = Article.objects.filter(id__in=[f for f in following])
        # ret = serializer(publish_list,many=True)

        return Response(baseResponse(data=articles.data))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(baseResponse(success="文章发表成功"), status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        record = UserReadAricle()
        record.user = request.user
        record.article = instance
        record.articleName = instance.name
        record.save()
        instance.click_num += 1
        instance.save()
        comment_ = Comment.objects.filter(article=instance).order_by('-time')
        comments = CommentSerializer(comment_, many=True)
        serializer = self.get_serializer(instance)
        return Response(articleResponse(article=serializer.data, comments=comments.data))
