from django.shortcuts import render

def acerca_de_mi(request):
    return render(request, 'informacion_app/acerca_de_mi.html')

def nosotros(request):
    return render(request, 'informacion_app/nosotros.html')
