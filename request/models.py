from django.db import models

# Create your models here.

from django.db import models
from account.models import User


class ItemRequest(models.Model):
    CATEGORY_CHOICES = [
        ("charger", "Charger"),
        ("battery", "Battery"),
        ("screen", "Screen"),
        ("keyboard", "Keyboard"),
        ("hinge", "Hinge"),
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("negotiating", "Negotiating"),
        ("bought", "Bought"),
        ("cancelled", "Cancelled"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="requests/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.category}"