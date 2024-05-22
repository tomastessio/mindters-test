from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/', views.ProductoListView.as_view(), name='success'),
]