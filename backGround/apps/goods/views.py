import random
from itertools import chain

from django.shortcuts import render
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.forms.models import model_to_dict
from articles.models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication, jwt_decode_handler

from utils.baseResponse import baseResponse
from .models import Goods, GoodsCategory
from .serializer import GoodsSerializer, CategorySerializer, GoodsShowSerializer
from .filter import GoodsFilter
from rest_framework.authentication import TokenAuthentication
import rest_framework.permissions as p


# Create your views here.
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def getform(request):
    return render(request, '留言板.html')


# class GoodsPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     page_query_param = 'p'
#     max_page_size = 100


class GoodsListViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # pagination_class = GoodsPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [p.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')

    def list(self, request, *args, **kwargs):
        l = Goods.objects.count()
        l1 = int(l / 2)
        lis = random_int_list(1, l, l1)
        good_list = Goods.objects.filter(id__in=[f for f in lis])
        ret = GoodsShowSerializer(good_list, many=True)  # queryset
        return Response(baseResponse(data=ret.data))


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        userid = request.user.id

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(baseResponse(data=serializer.data))


class GoodsListView(generics.ListAPIView):
    """
     商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # pagination_class = GoodsPagination

    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)
    #     return Response(goods_serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
