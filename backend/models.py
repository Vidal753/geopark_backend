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
    first_name = models.CharField(verbose_name="Nombres", max_length=100)
    last_name = models.CharField(verbose_name="Apellidos", max_length=200)
    city = models.ForeignKey(
        City, verbose_name="Cuidad", on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class News(models.Model):
    banner = models.ImageField(verbose_name="Imagen Banner", upload_to="images/")
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


class Image(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Titulo", max_length=50)
    image = models.ImageField(verbose_name="Imagen", upload_to="images/")

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

    img_preview.short_description = "Vista Previa"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"


class Video(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Titulo", max_length=50)
    miniature = models.ImageField(
        verbose_name="miniatura", upload_to="miniature/", null=True
    )
    video = models.FileField(upload_to="videos/", verbose_name="Video")

    def video_preview(self):
        return mark_safe(
            f"<video src='{self.video.url}' width='500' poster='{self.miniature.url}' controls controlsList='nodownload'/>"
        )

    video_preview.short_description = "Vista Previa"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


class Document(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Titulo", max_length=50)
    description = models.TextField(verbose_name="Descripción", max_length=400)
    poster = models.ImageField(verbose_name="Portada", upload_to="images/")
    document = models.FileField(upload_to="documents/", verbose_name="Documento")

    def img_preview(self):
        return mark_safe(f'<img src = "{self.poster.url}" width = "500"/>')

    img_preview.short_description = "Vista Previa"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
