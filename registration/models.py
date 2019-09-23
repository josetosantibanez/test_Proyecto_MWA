from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profiles/" + filename

class Tipo_Cuenta(models.Model):
    tipo = models.CharField(max_length = 20)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    rut = models.CharField(max_length=12, verbose_name = "Rut", null=True, blank=True)
    nombres = models.CharField(max_length=40, verbose_name = "Primer nombre", null=True, blank=True)
    apellido_p = models.CharField(max_length=40, verbose_name = "Apellido paterno", null=True, blank=True)
    apellido_m = models.CharField(max_length=40, verbose_name = "Apellido materno", null=True, blank=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True) 
    genero = models.CharField(max_length=1, verbose_name = "Genero", null=True, blank=True)
    direccion = models.CharField(max_length=50, verbose_name = "Nombres", null=True, blank=True) 
    celular = models.CharField(max_length=12, verbose_name = "Nombres", null=True, blank=True)
    correo = models.CharField(max_length=254, verbose_name="Email", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    tipo_cuenta = models.ForeignKey(Tipo_Cuenta, on_delete=models.CASCADE, default = 1)

@receiver(post_save, sender = User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")