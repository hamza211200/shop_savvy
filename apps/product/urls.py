from django.urls import path
from .views import get, get_id,add,update,delete

urlpatterns = [
    path('',get,name='get'),
    path('<int:product_id>/',get_id,name='get_product'),
    path('add',add,name='add'),
    path('update/<int:product_id>',update,name='update'),
    path('delete/<int:product_id>',delete,name='delete'),
]