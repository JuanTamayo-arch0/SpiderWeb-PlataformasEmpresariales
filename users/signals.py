from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Profile

@receiver(post_save, sender=User)
def asignar_rol_usuario(sender, instance, created, **kwargs):
    if created:
        try:
            grupo_usuario = Group.objects.get(name='Usuario')
            instance.groups.add(grupo_usuario)
        except Group.DoesNotExist:
            print("El grupo 'Usuario' no existe. Asegúrate de crearlo primero.")


@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.profile.save()