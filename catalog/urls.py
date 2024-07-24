from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('config.urls'))
]
urlpatterns = [
    path("admin/", admin.site.urls),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
]

from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    return render(request, 'catalog/contact.html')
