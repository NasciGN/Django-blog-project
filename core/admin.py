from django.contrib import admin
# Register your models here.

from core.models import Post

#  admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'dthr_Criado', 'status')  # COMANDO PARA LISTAR OS POSTS
    list_filter = ('status', 'dthr_Criado', 'autor', 'dthr_Publicado')  # COMANDO PARA MOSTRAR OS FILTROS DE PESQUISA
    search_fields = ('titulo', 'corpo')  # COMANDO PARA HABILITAR A PESQUISA DE POSTS
    prepopulated_fields = {'slug': ('titulo',)}  # PREENCHE O SLUG AUTOMATICAMENTE COM BASE NO TITULO
    raw_id_fields = ('autor',)  # HABILITA A PESQUISA DE AUTORES
    date_hierarchy = 'dthr_Publicado'
    ordering = ('status', 'dthr_Publicado')