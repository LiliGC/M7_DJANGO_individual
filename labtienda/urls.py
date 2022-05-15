from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('clientes/',views.clientes, name='clientes'),
    path('cliente_edit/<int:pk>',views.cliente_edit, name='cliente_edit'),
    path('cliente_delete/<int:pk>',views.cliente_delete, name='cliente_delete'),
    path('profesional/',views.profesional, name='profesional'),
    path('profesional_edit/<int:pk>',views.profesional_edit, name='profesional_edit'),
    path('profesional_delete/<int:pk>',views.profesional_delete, name='profesional_delete'),
    path('cliente_registro/',views.registro_cliente, name='cliente_registro'),
    path('register_user/',views.register_user, name='register_user'),
    path('registro_profesional/',views.registro_professional, name='registro_professional'),
    path('comentario/',views.comentario, name='comentario'),
    path('listacomentarios/',views.listacomentarios, name='listacomentarios'),
    path('comentario_edit/<int:pk>',views.comentario_edit, name='comentario_edit'),
    path('comentario_delete/<int:pk>',views.comentario_delete, name='comentario_delete'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
]