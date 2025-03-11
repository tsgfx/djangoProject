from django.shortcuts import render, redirect
from cookie_demo import models

# Create your views here.
def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库查询用户信息
        # 1. MySQL数据库，创建mysqlclient
        # 2. sqlite3数据库，文件数据库
        user_obj = models.UserInfo.objects.filter(name=username, password=password).first()
        if user_obj:
            # 如果成功：
            # 1.生成随机字符串
            # 2.返回给前端，前端保存到cookie中
            # 3.存储到网站的session中，随机字符串+用户信息
            # request.session['username'] = username
            # request.session['user_id'] = user_obj.id
            request.session['info'] = {'username': username, 'user_id': user_obj.id}
            return redirect('/home/')
        else:
            """
            如果失败：
            1.提示错误信息
            2.返回登录页面
            """
            return render(request, 'login.html', {'error': '用户名或密码错误'})


def home(request):
    """
    首页
    :param request:
    :return:
    """
    # 如果用户已经登录
    info = request.info_dict
    print(info)
    return render(request, 'home.html', {'info': info})

def order(request):
    """
    订单页面
    :param request:
    :return:
    """
    return render(request, 'order.html')
