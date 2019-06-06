from django.db import models
from clubes.models import Club

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length = 200, verbose_name = "Título")
    subtitulo = models.CharField(max_length = 200, verbose_name = "Subtítulo")
    cuerpo = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="noticias")
    url_noticia = models.URLField(verbose_name="Link de noticia",blank =True, null=True)
    club_id = models.ForeignKey(Club, verbose_name = "Codigo de club",on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add= True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now= True,verbose_name="Fecha de ult. actualizacion")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-created']

    
    def __str__(self):
        return self.titulo
