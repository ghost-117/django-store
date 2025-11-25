from django.shortcuts import render


def index(request):
    """
    Vista principal de la página de inicio
    Muestra la tienda
    """
    context = {
        'title': 'Inicio - Django Store',
        'welcome_message': 'Bienvenido a Django Store',
    }
    return render(request, 'home/index.html', context)