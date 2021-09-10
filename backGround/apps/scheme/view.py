import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters, permissions
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from goods.models import Goods
from goods.serializer import GoodsShowSerializer

from reason.models import Reason
from reason.serializer import ReasonSerializer
from tip.models import Tip
import random

from tip.serializer import TipSerializer
from utils.baseResponse import baseResponse, schemeResponse


# scheme是对reason和tip以及goods的整合
class SchemeListViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # pagination_class = GoodsPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    # filter出与用户type相对接的tip和commodities
    def list(self, request, *args, **kwargs):
        t = self.request.user.typ
        # t1 = Tip.objects.count()
        # len1 = int(t1 / 2)
        # lis1 = random_int_list(1, t1, len1)
        type_list = t.split()
        tip_list = Tip.objects.filter(typ__in=type_list)
        tip = TipSerializer(tip_list, many=True)  # queryset
        # t2 = Goods.objects.count()
        # len2 = int(t2 / 2)
        # lis2 = random_int_list(1, t2, len2)
        commodities_list = Goods.objects.filter(typ__in=type_list)
        commodities = GoodsShowSerializer(commodities_list, many=True)
        reason_ = Reason.objects.filter(typ__in=type_list)
        reason = ReasonSerializer(reason_, many=True)
        return Response(schemeResponse(tips=tip.data, commodities=commodities.data, todo=reason.data))
