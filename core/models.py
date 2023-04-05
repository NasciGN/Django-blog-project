from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PublicadosManager(models.Manager):
    def get_queryset(self):
       return super().get_queryset().filter(status='publicado')
    
class Post(models.Model):
    objects = models.Manager()
    publicados = PublicadosManager()
    STATUS_POST = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    corpo = models.TextField()
    status = models.CharField(max_length=9, choices=STATUS_POST, default='rascunho')
    dthr_Criado = models.DateTimeField(auto_now_add=True)
    dthr_Publicado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_autor')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-dthr_Publicado',)
    
    def __str__(self):
        return self.titulo