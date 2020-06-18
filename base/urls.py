from django.urls import path #Das urls do django, importa-se os caminhos.

from .views import index, contato, produto, vendedor
# Do modulo de views, importa-se as views declaradas


urlpatterns = [  #Declara-se as urls de cada view importada
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>', produto, name='produto'),
    path('vendedor/<int:id>', vendedor, name='vendedor'),
]
