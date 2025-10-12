from django.urls import path
from .views import add, get, get_item,get_id,get_item_by_id,get_order_id,delete,delete_order_item,update,update_items

urlpatterns = [
    path('',get,name='get'),
    path('<int:order_id>',get_id,name='get_id'),
    path('<int:order_id>/items',get_item,name='get_product'),
    path('<int:order_id>/order',get_order_id,name='get_order_id'),
    path('<int:order_id>/items_id',get_item_by_id,name='get_item_by_id'),
    path('add',add,name='add'),
    path('<int:order_id>/update',update,name='update'),
    path('<int:order_item_id>/update_item',update_items,name='upadate_item'),
    path('<int:order_id>/delete',delete,name='delete'),
    path('<int:order_item_id>/delete_item',delete_order_item,name='add'),

]