from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


# Create your views here.

class MeuSiteListView(APIView):
    def get(self, request, *arg, **kwargs):
        posts = Post.postobjects.all()[0:4] #[0:4] exibir apenas 4 post por pagina
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    def get(self, request, post_slug, *arg, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)