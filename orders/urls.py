from django.urls import path
from . import views

urlpatterns = [
    # 🧾 Checkout page
    path('checkout/', views.checkout, name='checkout'),

    # 🎉 Order success page
    path('success/', views.order_success, name='order_success'),
]