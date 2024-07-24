from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'catalog/index.html', context)

def contact(request):
    context = {}
    return render(request, 'catalog/contact.html', context)