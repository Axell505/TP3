from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Listar publicaciones
    path('create/', views.post_create, name='post_create'),  # Crear nueva publicación
    path('<int:id>/', views.post_detail, name='post_detail'),  # Ver detalle de publicación
    path('<int:id>/edit/', views.post_edit, name='post_edit'),  # Editar publicación
    path('<int:id>/delete/', views.post_delete, name='post_delete'),  # Eliminar publicación
]