from django.contrib import admin
from django.urls import path, include
from .views import prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba)
]