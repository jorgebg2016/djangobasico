from django.contrib import admin

from .models import Produto, Cliente, Vendedor #importa os modelos criados do modulo models

class ProdutoAdmin(admin.ModelAdmin): # Classe das informações de tabela que aparecem na sessão de admin
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin) #Registra os modelos na sessão administrativa do django
admin.site.register(Vendedor, VendedorAdmin)
