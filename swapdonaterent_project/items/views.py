from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Item, Conversation, Message
from .forms import ItemForm, MessageForm


def item_list(request):
    items = Item.objects.filter(is_active=True)

    # Filtering
    category = request.GET.get('category')
    item_type = request.GET.get('item_type')
    search = request.GET.get('search')

    if category:
        items = items.filter(category__id=category)
    if item_type:
        items = items.filter(item_type=item_type)
    if search:
        items = items.filter(Q(name__icontains=search) | Q(description__icontains=search))

    return render(request, 'items/item_list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/item_detail.html', {'item': item})


@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            messages.success(request, 'Item posted successfully!')
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {'form': form})


@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_form.html', {'form': form})


@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('my_items')
    return render(request, 'items/item_confirm_delete.html', {'item': item})


@login_required
def my_items(request):
    items = Item.objects.filter(owner=request.user)
    return render(request, 'items/my_items.html', {'items': items})


@login_required
def add_to_cart(request, item_id):
    from core.models import Cart, CartItem  # Import here to avoid circular import

    item = get_object_or_404(Item, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if item is already in cart
    if not CartItem.objects.filter(cart=cart, item=item).exists():
        CartItem.objects.create(cart=cart, item=item)
        messages.success(request, 'Item added to cart!')
    else:
        messages.info(request, 'Item is already in your cart.')

    return redirect('item_detail', pk=item_id)


@login_required
def remove_from_cart(request, item_id):
    from core.models import Cart, CartItem  # Import here to avoid circular import

    item = get_object_or_404(Item, id=item_id)
    cart = get_object_or_404(Cart, user=request.user)

    CartItem.objects.filter(cart=cart, item=item).delete()
    messages.success(request, 'Item removed from cart!')

    return redirect('cart_view')


@login_required
def cart_view(request):
    from core.models import Cart, CartItem  # Import here to avoid circular import

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'items/cart.html', {'cart_items': cart_items})



