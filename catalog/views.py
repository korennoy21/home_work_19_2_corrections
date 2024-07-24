from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        # Обработка данных формы обратной связи
        pass
    else:
        return render(request, 'contact.html')
