from django.urls import path
from floppa import views

app_name = 'floppa'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
]
