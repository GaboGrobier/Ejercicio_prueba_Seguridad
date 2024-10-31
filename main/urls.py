from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_vulnerable, name='login_vulnerable'),
    path('carrito/', views.carrito_view, name='carrito_view'),
    path('', views.index, name='index'),  # Página de inicio

]