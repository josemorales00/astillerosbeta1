from django.urls import path
from .views import homeView, abrirAPI, tabla

urlpatterns = [
    path('', homeView, name='home'),
    path('abrirAPI/', abrirAPI, name='abrirAPI'),
    path('tabla/', tabla, name='tabla')
]
