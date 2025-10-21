from django.contrib import admin
from .models import Category, Cart, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    list_filter = ['created_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'item', 'added_at']
    list_filter = ['added_at']
