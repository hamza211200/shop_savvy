from django.db import models
from django.conf import settings
from ..product.models import Product

# Create your models here.
class Order (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=[
        ("PENDING","Pending"),("PAID","Paid"),("SHIPPED","Shipped")],default="Pending")
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"