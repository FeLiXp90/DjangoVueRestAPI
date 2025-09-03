#Converter os campos para json da API

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','titulo','thumbnail','conteudo','slug','publicado','autor','status')