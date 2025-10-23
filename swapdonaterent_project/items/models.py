from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    ITEM_TYPES = [
        ('swap', 'Swap'),
        ('donate', 'Donate'),
        ('rent', 'Rent'),
    ]

    CONDITIONS = [
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Use string reference instead of direct import
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    condition = models.CharField(max_length=10, choices=CONDITIONS)
    location = models.CharField(max_length=200)
    contact_info = models.TextField()
    image = models.ImageField(upload_to='item_images/', default='default_item.jpg')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


