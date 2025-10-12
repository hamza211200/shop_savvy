from django.db import models
from django.conf import settings
from ..user.models import AbstractUser
from ..product.models import Product

# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    sentiment = models.CharField(max_length=20, blank=True)  # e.g., 'positive', 'neutral', 'negative'
    summary = models.TextField(blank=True)
    suggestions = models.JSONField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=[(i,i) for i in range (1,6)],default=1)


