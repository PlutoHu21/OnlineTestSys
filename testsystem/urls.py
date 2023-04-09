from django.urls import path

from . import views

app_name = 'testsystem'
urlpatterns = [
    path('', views.index),
    path('index/', views.index,name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('<int:paper_id>/', views.paper, name='paper'),
    path('<int:paper_id>/cal/', views.cal_score, name='calculate'),
    path('forgetpwd/',views.forgetpwd,name='forgetpwd'),
    path('download/',views.download,name='download'),
]
