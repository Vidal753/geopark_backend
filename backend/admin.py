from django.contrib import admin
from .models import City, User, News, Image, Video, Document


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "General",
            {"fields": ["username", "first_name", "last_name", "email", "city"]},
        ),
        (
            "Privacidad",
            {"fields": ["is_staff", "is_active", "password"]},
        ),
    ]

    list_display = ("username", "first_name", "last_name", "email", "city")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General", {"fields": ["title", "city", "date", "description"]}),
        ("Imagen", {"fields": ["banner", "img_preview"]}),
    ]
    list_display = ("title", "description", "date", "city")
    readonly_fields = ["img_preview"]
    list_filter = ["city"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "img_preview")
    readonly_fields = ["img_preview"]
    list_filter = ["city"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "city")
    readonly_fields = ["video_preview"]
    list_filter = ["city"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "city")
    readonly_fields = ["img_preview"]
    list_filter = ["city"]
