from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist, Category


# 🛍️ Product List (Search + Category Filter)
def product_list(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category__name__iexact=category)

    return render(
        request,
        'products/product_list.html',
        {
            'products': products,
            'categories': categories,
            'search': search,
            'category': category,
        }
    )


# 📄 Product Detail
def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )


# ❤️ Add to Wishlist
@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('wishlist')


# ❤️ Wishlist Page
@login_required
def wishlist(request):

    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(
        request,
        'products/wishlist.html',
        {
            'wishlist_items': wishlist_items
        }
    )


# ❌ Remove Wishlist
@login_required
def remove_wishlist(request, wishlist_id):

    item = get_object_or_404(
        Wishlist,
        id=wishlist_id,
        user=request.user
    )

    item.delete()

    return redirect('wishlist')