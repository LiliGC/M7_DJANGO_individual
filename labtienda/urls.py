from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('usuarios/',views.usuarios, name='usuarios'),
    path('registro/',views.registro_cliente, name='registro'),
    path('register_user/',views.register_user, name='register_user'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
]

