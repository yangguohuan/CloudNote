from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
from hashlib import md5

# Create your views here.
def index(request):
    return render(request, 'Users/index.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'Users/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_c = request.POST['password_c']
        if password != password_c:
            return HttpResponse('输入密码不一致')
        if Users.objects.filter(username=username):
            return HttpResponse('用户已存在')
        p = md5()
        p.update(password.encode())
        password = p.hexdigest()
        try:
            new_user = Users.objects.create(username=username, password=password)
        except Exception as e:
            print('用户已注册')
            return HttpResponse('用户已注册')
        request.session['username'] = username
        request.session['uid'] = new_user.id
        response = HttpResponse('注册成功')
        response.set_cookie('username', new_user.username, max_age=30*24*3600)
        response.set_cookie('password', new_user.password, max_age=30*24*3600)
        return response
    else:
        pass
    context = {}
    return render(request, "Users/index.html", context)


def login(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        try:
            user = Users.objects.get(username=username)
        except Exception as e:
            print('用户名重复')
            return HttpResponse('用户名或密码不正确')
        if username == user.username and password == user.password:
            request.session['username'] = username
            request.session['uid'] = user.id
            return HttpResponse('登入成功')
        else:
            return HttpResponse('登入失败')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        p = md5()
        p.update(password.encode())
        password = p.hexdigest()
        try:
            user = Users.objects.get(username=username)
        except Exception as e:
            print('用户名重复')
            return HttpResponse('用户名或密码不正确')
        if username == user.username and password == user.password:
            request.session['username'] = username
            request.session['uid'] = user.id
            response = HttpResponse('登入成功')
            if request.POST['rem'] == 'on':
                response.set_cookie('username', user.username, max_age=30*24*3600)
                response.set_cookie('password', user.password, max_age=30*24*3600)
            return response
        else:
            return HttpResponse('登入失败')
    else:
        pass