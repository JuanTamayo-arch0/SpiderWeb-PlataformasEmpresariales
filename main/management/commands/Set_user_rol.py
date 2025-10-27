from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Asigna un rol (grupo) a un usuario existente, eliminando todos los anteriores'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True, help='Nombre de usuario')
        parser.add_argument('--rol', type=str, required=True, help='Nombre del rol (grupo)')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        rol = kwargs['rol']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f'Usuario "{username}" no existe.')

        try:
            grupo = Group.objects.get(name=rol)
        except Group.DoesNotExist:
            raise CommandError(f'Grupo/rol "{rol}" no existe. Crea el grupo primero.')

        user.groups.set([grupo])
        user.save()

        self.stdout.write(self.style.SUCCESS(
            f'Rol anterior eliminado. Rol "{rol}" asignado al usuario "{username}" correctamente.'
        ))