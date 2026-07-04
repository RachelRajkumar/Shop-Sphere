from django.urls import path
from . import views

urlpatterns = [
    # 🛒 View cart page
    path('', views.view_cart, name='view_cart'),

    # ➕ Add product to cart
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # ❌ Remove item from cart
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # 🔼 Increase quantity
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),

    # 🔽 Decrease quantity
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
]