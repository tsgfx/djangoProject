from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    # http://localhost:8000/login/
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证数据
        if username == 'admin' and password == '123456':
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

def index(request):
    # 从数据库中获取数据
    query_set = [
        {"id": 1, "phone": "13800138000", "name": "张三"},
        {"id": 2, "phone": "13800138001", "name": "李四"},
        {"id": 3, "phone": "13800138002", "name": "王五"},
        {"id": 4, "phone": "13800138003", "name": "赵六"},
    ]
    # 渲染模板
    return render(request, 'index.html', {'query_set': query_set})
