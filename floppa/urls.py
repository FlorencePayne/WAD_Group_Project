from django.urls import path
from floppa import views


app_name = 'floppa'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('login/', views.signin, name='login'),
    path('login/account/', views.account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('necklaces/', views.necklaces, name='necklaces'),
    
    path('necklaces/add_necklace/', views.add_necklace, name='add_necklace'),
    path('necklaces/<slug:necklace_name_slug>/', views.necklace, name="necklace"),
    path('cart/checkout/payment_confirmed/', views.payment_confirmed, name='payment_confirmed'),

]

