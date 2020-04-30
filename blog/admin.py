from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author', 'published', 'post_categories' )
    ordering = ('author', 'published')
    #los campos al ser tuplas se necesita dejar una , al final
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    #Crear una propia columna y la ordena
    def post_categories(self,obj):
        return ", ".join(i.name for i in obj.categories.all().order_by("name"))
    #Permite nombrar de otra manera
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)