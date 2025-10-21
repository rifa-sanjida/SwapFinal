def cart_count(request):
    if request.user.is_authenticated:
        from .models import Cart, CartItem  # Import here to avoid circular import
        cart, created = Cart.objects.get_or_create(user=request.user)
        count = CartItem.objects.filter(cart=cart).count()
        return {'cart_count': count}
    return {'cart_count': 0}

def categories(request):
    from .models import Category  # Import here to avoid circular import
    categories = Category.objects.all()
    return {'categories': categories}

def unread_messages_count(request):
    if request.user.is_authenticated:
        from items.models import Message  # Import here to avoid circular import
        count = Message.objects.filter(conversation__participants=request.user, read=False).exclude(sender=request.user).count()
        return {'unread_messages_count': count}
    return {'unread_messages_count': 0}
