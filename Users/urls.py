from django.urls import path

from Users import views

app_name = 'Users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
]