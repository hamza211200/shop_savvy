from django.urls import path
from . import views


urlpatterns = [ 
    path('',views.get,name="get"),
    path('<int:user_id>',views.get_by_id,name="get by id"),
    path('add',views.add,name='add'),
]