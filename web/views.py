from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
# Create your views here.
def login(request):
    # return HttpResponse("登录页面")
    return render(request, 'login.html')
    # return redirect('https://www.baidu.com')

def user_list(request):
    # 1. 获取所有用户信息
    data = ["user1", "user2", "user3"]
    mapping = {"user1": "用户1", "user2": "用户2", "user3": "用户3"}
    # 2.打开文件并读取数据
    # 3.模板渲染+文本替换
    return render(request, 'user_list.html', {'message': "用户列表", 'user_list': data, 'mapping': mapping})

def phone_list(request):
    # 1. 获取所有用户信息
    query_set = [
        {"id":1, "phone": "13800138000", "name": "张三"},
        {"id":2, "phone": "13800138001", "name": "李四"},
        {"id":3, "phone": "13800138002", "name": "王五"},
        {"id":4, "phone": "13800138003", "name": "赵六"},
    ]
    # 2.模板渲染+数据传递，以表格形式展示
    return render(request, 'phone_list.html', {'query_set': query_set})
