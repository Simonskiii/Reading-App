from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend

from users.tasks import send_register_email
from utils.baseResponse import baseResponse
from utils.email_send import random_str
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm

from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from random import choice
from rest_framework import mixins, viewsets, status, permissions, authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import VerifyCode
from .serializers import SmsSerializer, EmailSerializer, UserRegSerializer, UserDetailSerializer, UserProfileSerializer
import logging
logger = logging.getLogger('django')#这里的日志记录器要和setting中的loggers选项对应，不能随意给参



# Create your views here.

User = get_user_model()


class UserProfileViewset(viewsets.GenericViewSet, UpdateModelMixin, ListModelMixin):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(baseResponse(success="更改成功"))


# 用户视图集,包括注册,更新和retrieve
class UserViewSet(CreateModelMixin, viewsets.GenericViewSet, UpdateModelMixin, RetrieveModelMixin):
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # payload = jwt_payload_handler(user)
        # re_dict["token"] = jwt_encode_handler(payload)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(baseResponse(success="注册成功"), status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class RegisterViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        email_record = VerifyCode()
        code = random_str(6)
        email_record.code = code
        email_record.email = email
        email_record.send_type = "register"
        send_register_email(email, code)
        email_record.save()
        return Response(baseResponse(success="验证码已发送"), status=status.HTTP_201_CREATED)


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username))
            if user.check_password(password):
                logger.info('[Success] ' + "登录成功")
                return user
            logger.error('[Error] ' + "登录失败")
        except Exception:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

