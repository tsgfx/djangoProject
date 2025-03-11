"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from web.views import login
# from web.views import user_list
# from web import views
# from demo import views
from department import views
# from cookie_demo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', login),
    # path('user_list/', user_list),
    # path('phone_list/', views.phone_list)
    # path('login/', views.login),
    # path('index/', views.index)
    # path('depart/', views.depart),
    path('get_depart_list/', views.get_depart_list),
    path('add_department/', views.add_department),
    path('delete_department/', views.delete_department),
    path('edit_department/', views.edit_department),
    path('get_employee_list/', views.get_employee_list),
    path('add_employee/', views.add_employee),
    path('get_order/', views.get_order)
    # path('login/', views.login),
    # path('home/', views.home),
    # path('order/', views.order),
]
