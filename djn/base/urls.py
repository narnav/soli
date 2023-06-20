
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    # path('products', views.products),
    path('prods', views.ProductViewSet.as_view()),
    path('prods/<pk>', views.ProductViewSet.as_view()),
    # path('orders', views.CartView.as_view()),
    path('checkout', views.CartView.as_view()),
    path('login/', TokenObtainPairView.as_view()),

]
