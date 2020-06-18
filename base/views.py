from django.shortcuts import render, get_object_or_404 #(busca o objeto da requisição ou retorna o erro 404)
from .models import Produto, Vendedor
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    print(request)  # printa: <WSGIRequest: GET '/'>; WSGI é o padrão de aplicações python para a web, GET é o metodo da requisição, e '/' é a url da raiz(onde a requisição está sendo feita)
    print(f'User: {request.user}')

    if str(request.user) == 'AnonymousUser':
        status = "Nenhum usuário logado"
    else:
        status = request.user

    produtos = Produto.objects.all()
    vendedores = Vendedor.objects.all()
    context = {
        'status': status,
        'produtos': produtos,
        'vendedores': vendedores
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    # print(f'ID: {id}')
    # dados_produto = Produto.objects.get(id=id)
    dados_produto = get_object_or_404(Produto, id=id) #procura os objeto da classe Produto que possuem um id dado, e caso não encontrar, retorna o erro 404
    context = {
        'produto': dados_produto
    }
    return render(request, 'produto.html', context)

def vendedor(request, id):
    dados_vendedor = Vendedor.objects.get(id=id)
    context = {
        'vendedor': dados_vendedor
    }
    return render(request, 'vendedor.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=500)
