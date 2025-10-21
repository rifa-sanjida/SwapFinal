from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('<int:pk>/update/', views.item_update, name='item_update'),
    path('<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('my-items/', views.my_items, name='my_items'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('conversations/', views.conversations, name='conversations'),
    path('conversations/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    path('start-conversation/<int:item_id>/', views.start_conversation, name='start_conversation'),
]
