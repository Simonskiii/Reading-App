from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueTogetherValidator

from user_operations.models import UserReadAricle, UserFavAricle, Comment


# 阅读记录Serializer,只用于get
class UserReadArticleSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()
    time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserReadAricle
        fields = ('articleName', 'time', 'article')


# 评论Serializer,用于get
class CommentSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()
    time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Comment
        fields = ('article', 'content', 'time', 'userName', 'articleName')


# 评论Serializer,用于post
class CommentCreateSerializer(ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('user', 'article', 'content', 'articleName', 'userName')


# 收藏Serializer,用于get
class UserFavArticleSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()
    time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserFavAricle
        fields = ('articleName', 'time', 'article')


# 收藏Serializer,用于post
class UserFavArticleCreateSerializer(ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFavAricle
        validators = [
            UniqueTogetherValidator(
                queryset=UserFavAricle.objects.all(),
                fields=('user', 'article'),
                message="已经收藏"
            )
        ]
        fields = ('user', 'article', 'articleName')

