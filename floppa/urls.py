from django.urls import path
from floppa import views

app_name = 'floppa'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('login/', views.login, name='login'),
    path('login/account/', views.account, name='account'),
    path('login/account/wishlist', views.wishlist, name='wishlist'),
    path('signup/', views.signup, name='signup'),
    path('necklaces/', views.necklaces, name='necklaces'),
]