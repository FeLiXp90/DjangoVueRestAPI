from django.contrib import admin
from django.urls import path, include

#importar bibliotecas para trabalhar com imagens

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #importando URLS da APP meusite
    path('meusite/', include('meusite.urls', namespace="meusite")),
    path('api-auth', include('rest_framework.urls'))

]

#adicionar os urls static e media

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)