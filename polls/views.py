# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from.models import *
import random

def toLogin_view(request):
    return render(request,'login.html')

def Login_view(request):
    u=request.POST.get("user",'')
    p=request.POST.get("pwd",'')
    if u and p:
        c=StudentInfo.objects.filter(stu_name=u,stu_pwd=p).count()
        if c>=1:
            return HttpResponse('登录成功！')
        else:
            return HttpResponse('账号密码错误！')
    else:
        return HttpResponse('请输入正确的账号密码。')

#渲染注册界面
def toregister_view(request):
    return render(request,'register.html')

#点击注册后做的逻辑判断
def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    if u and p:
        stu=StudentInfo(stu_id=str(random.randrange(00000,99999)),stu_name=u,stu_pwd=p)
        stu.save()
        return  HttpResponse('注册成功！')
    else:
        return HttpResponse('请输入完整的账户和密码！')

def test1_view(request):
    s = request.POST.get("frame",'')
    return  HttpResponse('first name:'+s)



def totest1_view(request):
    return render(request,'test1.html')