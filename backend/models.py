from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe


# Create your models here.
class City(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class User(AbstractUser):
    city = models.OneToOneField(
        City, verbose_name="Cuidad", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class News(models.Model):
    banner = models.ImageField(
        null=True, blank=True, upload_to="images/", verbose_name="Imagen Banner"
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Cuidad")
    title = models.CharField(verbose_name="Titulo", max_length=50)
    date = models.DateField(verbose_name="Fecha")
    description = models.TextField(verbose_name="Descripción", max_length=200)

    def img_preview(self):
        return mark_safe(f'<img src = "{self.banner.url}" width = "300"/>')

    img_preview.short_description = "Vista Previa"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
