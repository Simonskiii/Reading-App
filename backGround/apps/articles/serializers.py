
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from users.mUniqueValidator import mValidationError
from utils.baseResponse import baseResponse
from .models import Article, ArticleCatergory


# 用于list的articleSerializer
class AritcleShowSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('name', 'content', 'author', 'click_num', 'id', 'fav_num')
        # list_serializer_class = IsActiveListSerializer


# 用于retrieve的ArticleSerializer
class AritcleRetrieveSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()
    time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Article
        fields = ('name', 'content', 'fav_num', 'author', 'id', 'comment_num', 'time')

    # def get_usagedata(self, obj):
    #     return models.Article.objects.filter(name='media').count()


# 用于crete的ArticleSerializer
class AriticleCreateSerializer(Serializer):
    name = serializers.CharField(max_length=20, required=True, help_text='题目')
    content = serializers.CharField(required=True, help_text='内容')

    def validate_name(self, name):
        if Article.objects.filter(name=name).count():
            raise mValidationError(detail=baseResponse(error="文章已存在"))
        return name

