from django.contrib import admin
from .models import City, User, News


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
    list_display = ("title", "description", "date", "city")
    list_filter = ["city"]
