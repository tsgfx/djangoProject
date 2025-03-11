# 作者: 郭瑞超
# 2025年03月11日13时31分40秒
# grcsxb269@163.com
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 如果是登录页面，则不进行登录验证
        if request.path == '/login/':
            print("login MyMiddleware process_request")
            return
        # 无返回值或返回None，render, redirect
        # 有返回值，继续执行
        print("MyMiddleware process_request")

        info_dict = request.session.get('info')

        if info_dict:
            request.info_dict = info_dict
            return
        return redirect('/login/')

    def process_response(self, request, response):
        print("MyMiddleware process_response")
        return response
