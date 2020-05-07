from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    listaDeProdutos = Product.objects.all()
    context = {
            'produtos': listaDeProdutos
    }
    return render (request, 'index.html', context)