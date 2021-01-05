from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gererproduit, name='gererproduit'),
    path('<int:id>/', views.detailProduit, name="detailProduit"),# Expression régulière

    path('cart/add/<int:id>/', views.ajout_article, name='ajout_article'),
    path('cart/item_clear/<int:id>/', views.suppression_article, name='suppression_article'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('Panier',views.panier,name='panier'),
]