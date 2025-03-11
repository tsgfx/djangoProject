from django import forms
from django.shortcuts import render, redirect, HttpResponse
from department import models
from django.core.validators import RegexValidator


# Create your views here.
def depart(request):
    # 新增
    # models.Department.objects.create(title='销售部', count=100)
    # models.Department.objects.create(**{'title': '财务部', 'count': 50})

    # 查询
    # query_set = models.Department.objects.all()
    # query_set = models.Department.objects.filter(title='销售部')
    # for obj in query_set:
    # print(obj.id,obj.title, obj.count)

    # 删除
    # models.Department.objects.all().first().delete()
    # models.Department.objects.filter(title='销售部').delete()
    # query_set = models.Department.objects.all()
    # for obj in query_set:
    #     print(obj.id, obj.title, obj.count)

    return HttpResponse("Department Page")


def get_depart_list(request):
    """
    获取部门列表
    :param request:
    :return:
    """
    queryset = models.Department.objects.all()
    return render(request, 'department_list.html', {'department_list': queryset})


def add_department(request):
    """
    添加部门
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'add_department.html')
    else:
        title = request.POST.get('title')
        count = request.POST.get('count')
        models.Department.objects.create(title=title, count=count)
        return redirect('/get_depart_list/')


def delete_department(request):
    """
    删除部门
    :param request:
    :return:
    """
    department_id = request.GET.get('id')
    models.Department.objects.filter(id=department_id).delete()
    return redirect('/get_depart_list/')


def edit_department(request):
    """
    编辑部门
    :param request:
    :return:
    """
    if request.method == "GET":
        department_id = request.GET.get('id')
        selected_department = models.Department.objects.filter(id=department_id).first()
        return render(request, 'edit_department.html', {'current_department': selected_department})
    else:
        department_id = request.GET.get('id')
        title = request.POST.get('title')
        count = request.POST.get('count')
        models.Department.objects.filter(id=department_id).update(title=title, count=count)
        return redirect('/get_depart_list/')


def get_employee_list(request):
    """
    获取员工列表
    :param request:
    :return:
    """
    queryset = models.Employee.objects.all()
    return render(request, 'employee_list.html', {'employee_list': queryset})


def add_employee(request):
    """
    添加员工
    :param request:
    :return:
    """
    if request.method == "GET":
        # 获取所有部门信息
        department_list = models.Department.objects.all()
        return render(request, 'add_employee.html', {'department_list': department_list})
    else:
        employee_name = request.POST.get('name')
        employee_salary = request.POST.get('salary')
        employee_department = request.POST.get('department')
        models.Employee.objects.create(name=employee_name, salary=employee_salary, department_id=employee_department)
        # 获取表单数据
        return redirect('/get_employee_list/')

class OrderForm(forms.Form):
    order_name = forms.CharField(label="商品名称", max_length=100, validators=[RegexValidator(r'^[a-zA-Z0-9\u4e00-\u9fa5]+$', message='请输入正确的商品名称')])
    order_address = forms.CharField(label="商品地址", widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=200)
    order_choices = forms.ChoiceField(label="商品选择", choices=[('1', '商品1'), ('2', '商品2'), ('3', '商品3')])

def get_order(request):
    if request.method == 'GET':
        form = OrderForm(initial={'order_name': '郭瑞超'})
        return render(request, 'order.html', {'form': form})
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid():
            print("成功", form.cleaned_data)
            return HttpResponse("成功")
        else:
            print("失败", form.errors)
            return render(request, 'order.html', {'form': form})