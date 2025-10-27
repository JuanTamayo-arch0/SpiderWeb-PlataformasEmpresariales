from django.urls import path
from .views import home, admin_only_view, editar_variant, eliminar_variant, agregar_variant, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('admin-only/', admin_only_view, name='admin_only'),
    path('editar/<int:id>/', editar_variant, name='editar_variant'),
    path('eliminar/<int:id>/', eliminar_variant, name='eliminar_variant'),
    path("agregar/", agregar_variant, name="agregar_variant"),
    path("perfil/", user_profile, name="perfil"),
]
