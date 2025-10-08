from .models import Product
import json

def get_product(request):
    return list(Product.objects.values('name','description','price','stock','created_at'))


def get_product_id(request,product_id):
    product = Product.objects.filter(id=product_id).values('name','description','price','stock','created_at').first()
    
    if product:
        return {"product":product}
    else:
        return {"message":f"{product_id} this product is not here."}
    
def add_product(request):
    data =json.loads(request.body)
    Product.objects.create(name = data.get("name"),description = data.get("description"),price=data.get("price"),stock=data.get("stock"))

    return{"message":"product is added successfully"}

def update_product(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return {f"{product_id} this product is not in the list"}
    data = json.loads(request.body)
    product.name = data.get('name')
    product.description = data.get('description')
    product.price = data.get('price')
    product.stock = data.get('stock')
    product.save()
    return {"message":"the product is updated successfully"}

def delete_product(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return {f"{product_id} this product is not in the list"}
    
    product.delete()
    return {"message":"the product is deleted successfully"}
    


