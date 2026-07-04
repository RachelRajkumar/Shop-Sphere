from django.urls import path
from . import views

urlpatterns = [
    # Register
    path(
        'register/',
        views.register,
        name='register'
    ),

    # Login
    path(
        'login/',
        views.user_login,
        name='login'
    ),

    # Logout
    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    # Delete Account
    path(
        'delete-account/',
        views.delete_account,
        name='delete_account'
    ),
]