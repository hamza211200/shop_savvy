from .models import Order, OrderItem
from ..product.models import Product
from ..user.models import Profile
import json
import datetime



def get_orders(request):
    return list(Order.objects.values("id","user","created_at","status"))

def get_order_by_id (request,order_id):
    order = Order.objects.filter(id=order_id).values("id","user","created_at","status").first()
    if order:
        return {"order":order}
    else :
        return {"error":f"{order_id} is no such order in the list"} 

def get_order_items(request, order_id):
    return list(OrderItem.objects.filter(order__id = order_id).values("id","order","product","quantity"))

def get_order_item_by_id(request, order_id, order_item_id):
    item = OrderItem.objects.filter(order__id = order_id, id=order_item_id).values("id", "order__status", "product__name", "quantity").first()
    
    if item:
        return {"item": item}
    else:
        return {"message": f"Neither order_id {order_id} nor order_item_id {order_item_id} exist."}

    
def add_order(request):
    data =json.loads(request.body)
    items = data.get("items", [])
    order = Order.objects.create(user = Profile.objects.get(id=request.user_id),
                           created_at = datetime.datetime.utcnow())
    
    # Add order items
    for item in items:
        product_id = item.get("product_id")
        quantity = item.get("quantity")

        # Check product existence
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return {"error": f"Product with id {product_id} not found"}

        # Create order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )

    return {"message" : "order created successfully."}

def update_order(request,order_id):
    try:
        order =Order.objects.get(id=order_id)
    except:
        return {"messgae": f"{order_id} not found here"}
    
    data = json.loads(request.body)
    # order.id = data.get("id")
    order.user = data.get("user")
    order.status = data.get("status")
    order.save()
    return {"message":"order updated successfully"}

def update_item(request,order_item_id):
    try:
        item = OrderItem.objects.get(id = order_item_id)
    except:
        return {"message" : f"{order_item_id} is not here"}
     
    data = json.loads(request.body)
    item.order = data.get("order")    
    item.product = data.get("product")    
    item.quantity = data.get("quantity")
    item.save() 
    return {"message": "item updated successfully"}

def delete_order(request,order_id):
    try:
        order = Order.objects.get(id =order_id)
    except:
        return {"message" : f"{order_id} is not in the database"}

    order.delete()
    return {"message" : "order deleted successfully"}


def delete_item(request,order_item_id):
    try:
        item = OrderItem.objects.get(id= order_item_id)
    except : 
        return {"message" : f"{order_item_id} is not in the database"}
    
    item.delete()
    return {"message":"the item is deleted successfully."}