from django.urls import path
from .views import MeuSiteListView
from .views import PostDetailView

app_name="meusite"

urlpatterns = [
    path('post/', MeuSiteListView.as_view()), #quando chamar essa URL ela chama as postagens
    path('post/<post_slug>/', PostDetailView.as_view()) #vai chamar somente o post do "slug" passado
]