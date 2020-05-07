from django.shortcuts import render
from core.models import Product
# Create your views here.
#def index(request):
  #  return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    listaDeProdutos = Product.objects.all()
    context = {
        'produto': listaDeProdutos
    }
    return render(request, 'index.html', context)