from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBlog/', include('AppBlog.urls')),
    path('AppRegistro/', include('AppRegistro.urls')),
]
