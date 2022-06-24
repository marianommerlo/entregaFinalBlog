from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('finanzaspersonales/', finanzaspersonales, name = 'finanzaspersonales'),
    path('inversiones/', inversiones, name = 'inversiones'),
    path('seguros/', seguros, name = 'seguros'),
    path('aboutMe/', aboutMe, name = 'aboutme'),
    path('noFunciona/', noFunciona, name = 'nofunciona'),
    path('post/<slug:slug>/', detallePost, name = 'detallePost'),
    
]