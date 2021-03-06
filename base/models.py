from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):  # Quando for apresntar um objeto, apresenta o nome dele
        return f'{self.nome}'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):  # Quando for apresntar um objeto, apresenta o nome dele
        return f'Nome:{self.nome} {self.sobrenome}'

class Vendedor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):  # Quando for apresntar um objeto, apresenta o nome dele
        return f'Nome:{self.nome} {self.sobrenome}'
