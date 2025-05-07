
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('loja/', include('loja.urls')),
    path('flappyCat/', include('flappyCat.urls')),
    path('skyF/', include('skyF.urls')),
    path('sobre/', include('sobre.urls')),
    path('toTheHel/', include('toTheHel.urls')),
    path('trabalheConosco/', include('trabalheConosco.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', include('django.contrib.auth.urls')),
]

