from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    return render(request, 'catalog/contact.html')
