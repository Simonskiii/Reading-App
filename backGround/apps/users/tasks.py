
from backGround.celery import app
from django.conf import settings

from backGround.settings import EMAIL_FROM
from users.models import VerifyCode
from utils.asynchronous_send_mail import send_mail
from utils.email_send import random_str


@app.task
def send_register_email(email, code):
    email_title = '激活链接'
    email_body = '同志您好，您的验证码是：{0}'.format(code)
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    return send_status

