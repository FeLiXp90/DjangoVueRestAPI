from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

def user_directory_path(instance, filename):
    return 'meusite/{0}/{1}'.format(instance.titulo, filename)

class Post(models.Model):

    class PostObjects(models.Model):
        def  get_queryset(self):
            return super().get_queryset() .filter(status= 'publicado')

    opcoes = (
        ('rascunho', 'Rascunho'), ('publicado', 'Publicado')
    )

    titulo = models.CharField(max_length=75)
    thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    excecao = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publicado', null=False, unique=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meusite_user')
    status= models.CharField(max_length=10, choices=opcoes, default='rascunho')
    objects = models.Manager()
    OPostObjects = PostObjects()

    #ordenar por ordem de postagem

    class Meta:
        ordering = ('-publicado', )
    
    def __str__(self):
        return self.titulo