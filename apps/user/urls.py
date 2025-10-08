from django.urls import path
from .views import get,get_id,add, login,update,change_password

urlpatterns =[
    path('',get,name = "get_user"),
    path('<int:user_id>',get_id,name= "get_userby_id"),
    path('register',add,name= "register"),
    path('login',login,name= "login"),
    path('update',update,name= "update"),
    path('change-password',change_password,name= "change-password"),
]