
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('perfil/', include('perfil.urls')),
    path('flappyCat/', include('flappyCat.urls')),
    path('skyF/', include('skyF.urls')),
    path('sobre/', include('sobre.urls')),
    path('toTheHel/', include('toTheHel.urls')),
    path('trabalheConosco/', include('trabalheConosco.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
