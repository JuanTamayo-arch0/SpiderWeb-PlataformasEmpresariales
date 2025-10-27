from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro_inicio, name='foro_inicio'),
    path('board/<slug:slug>/', views.ver_board, name='ver_board'),
    path('board/<slug:slug>/nuevo/', views.crear_post, name='crear_post'),
    path('crear_board/', views.crear_board, name='crear_board'),
    path('eliminar-post/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('banear-usuario/<int:user_id>/', views.banear_usuario, name='banear_usuario'),
    path('eliminar-respuesta/<int:respuesta_id>/', views.eliminar_respuesta, name='eliminar_respuesta'),
]