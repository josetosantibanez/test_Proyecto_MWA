from django.contrib import admin
from django.urls import path, include
from noticias.urls import noticias_patterns
from miembros.urls import miembros_patterns
from productos.urls import productos_patterns
from eventos.urls import eventos_patterns
from clubes.urls import clubes_patterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #Path Home
    path('', include("core.urls")),

    #Path de clubes
    path('clubes', include(clubes_patterns)),

    #Path de noticias
    path('club/noticias/',include(noticias_patterns)),

    #Path de miembros
    
    path('club/miembros/', include(miembros_patterns)),

    #Path de productos
    path('club/productos/', include(productos_patterns)),

    #Path de eventos
    path('club/eventos/', include(eventos_patterns)),

    #Path del auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


#Media
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)