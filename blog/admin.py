from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}

#Outra forma de fazer sem decorador
#admin.site.register(Post, PostAdmin)