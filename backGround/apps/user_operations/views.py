from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from articles.models import Article
from user_operations.models import UserReadAricle, UserFavAricle, Comment
from user_operations.serializers import UserReadArticleSerializer, UserFavArticleSerializer, \
    UserFavArticleCreateSerializer, CommentSerializer, CommentCreateSerializer
from utils.baseResponse import baseResponse


User = get_user_model()


# 阅读记录视图集,对get请求返回该用户所有阅读记录
class UserReadArticleViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    # pagination_class = GoodsPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        history_ = UserReadAricle.objects.filter(user=user).order_by('-time')
        history = UserReadArticleSerializer(history_, many=True)
        return Response(baseResponse(data=history.data))


# 收藏记录视图集,对get请求返回该用户所有阅读记录,可以post请求而产生新记录
class UserFavArticleViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        history_ = UserFavAricle.objects.filter(user=user).order_by('-time')
        history = UserFavArticleSerializer(history_, many=True)
        return Response(baseResponse(data=history.data))

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavArticleSerializer
        elif self.action == "create":
            return UserFavArticleCreateSerializer

        return UserFavArticleCreateSerializer

    def create(self, request, *args, **kwargs):
        article_id = request.data['article']
        article_name = Article.objects.get(id=article_id).name
        data = request.data.copy()
        data.update({'articleName': article_name})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(baseResponse(success="收藏成功"), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        article = instance.article
        article.fav_num += 1
        article.save()


# 评论视图集,对get请求返回该用户所有阅读记录,可以post请求而产生新记录
class CommentViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    # pagination_class = GoodsPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        history_ = Comment.objects.filter(user=user).order_by('-time')
        history = CommentSerializer(history_, many=True)
        return Response(baseResponse(data=history.data))

    def get_serializer_class(self):
        if self.action == "list":
            return CommentSerializer
        elif self.action == "create":
            return CommentCreateSerializer
        return CommentSerializer


    def create(self, request, *args, **kwargs):
        article_id = request.data['article']
        user_id = request.user.id
        article_name = Article.objects.get(id=article_id).name
        user_name = User.objects.get(id=user_id).name
        data = request.data.copy()
        data.update({'articleName': article_name})
        data.update({'userName': user_name})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(baseResponse(success="评论成功"), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        article = instance.article
        article.comment_num += 1
        article.save()

