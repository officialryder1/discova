from django.urls import path
from .views import *

urlpatterns = [
    # Application default url calls
    path('', Home, name="home"),
    path('store', Store, name='store'),
    path('detail/<int:pk>', detail, name='detail'),
    path('category/<str:cat>', category, name='category'),
    path('search', search, name='search'),
    path('profile', Profile, name="profile"),

    # User vendor autherntication url calls
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),

    # Vendors action calls on a product
    path('upload_product', upload_product, name='upload'),
    path('update_product/<int:pk>', update_product, name='update'),
    path('delete_product/<int:pk>', delete, name='delete_product'),
]
