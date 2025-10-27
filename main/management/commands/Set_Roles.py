# your_app/management/commands/crear_roles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from forum.models import Board, Post, Reply
from main.models import SpidermanVariant
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crea roles y asigna permisos para usuarios, Admin_foro y Admin_elementos'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # ROL: Usuario
        usuario_group, _ = Group.objects.get_or_create(name='Usuario')
        usuario_perms = [
           
            Permission.objects.get(codename='view_board'),
            Permission.objects.get(codename='add_post'),
            Permission.objects.get(codename='view_post'),
            Permission.objects.get(codename='add_reply'),
            Permission.objects.get(codename='view_reply'),
            Permission.objects.get(codename='view_spidermanvariant'),
            Permission.objects.get(codename='change_user'),
            Permission.objects.get(codename='view_user'),
        ]
        usuario_group.permissions.set(usuario_perms)

        # ROL: Admin_foro
        foro_group, _ = Group.objects.get_or_create(name='Admin_foro')
        foro_perms = usuario_perms + [
            Permission.objects.get(codename='add_board'),
            Permission.objects.get(codename='delete_board'),
            Permission.objects.get(codename='delete_post'),
            Permission.objects.get(codename='delete_reply'),
            Permission.objects.get(codename='change_profile'),  # Para banear
        ]
        foro_group.permissions.set(foro_perms)

        # ROL: Admin_elementos
        elementos_group, _ = Group.objects.get_or_create(name='Admin_elementos')
        elementos_perms = [
            Permission.objects.get(codename='add_spidermanvariant'),
            Permission.objects.get(codename='delete_spidermanvariant'),
            Permission.objects.get(codename='change_spidermanvariant'),
            Permission.objects.get(codename='view_spidermanvariant'),
        ]
        elementos_group.permissions.set(elementos_perms)

        self.stdout.write(self.style.SUCCESS("✅ Roles y permisos creados correctamente."))
