from django.urls import path
from floppa import views

app_name = 'floppa'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('account/', views.account, name='account'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]