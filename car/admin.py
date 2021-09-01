from django.contrib import admin

from .models import Car, PostImage
from user.models import CustomUser


class PostImageAdmin(admin.StackedInline):
    model = PostImage



@admin.register(Car)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Car


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser)