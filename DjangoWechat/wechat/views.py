# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.shortcuts import render, render_to_response, HttpResponse

# add wechat-token
from django.views.decorators.csrf import csrf_exempt  # 解除csrf验证
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

# Create your views here.

def home(request):
    return render_to_response('index.html')

# add wechat-token
conf = WechatConf(  # 实例化配置信息对象
    # 服务器配置-token
    # 公众号开发信息-开发者ID - appid
    # 公众号开发信息-开发者密码 - appsecret
    # 服务器配置-明文模式 -  encrypt_mode
    # 服务器配置-EncodingAESKey - encoding_aes_key
)


@csrf_exempt  # 去除csrf验证
def wechat(request):
    signature = request.GET.get('signature')  # 获取请求信息
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    wechat_instance = WechatBasic(conf=conf)  # 实例化微信基类对象
    if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):  # 检查验证请求的签名
        return HttpResponseBadRequest('Verify Failed')
    else:
        if request.method == 'GET':
            return HttpResponse(request.GET.get('echostr', None))  # 返回请求中的回复信息
