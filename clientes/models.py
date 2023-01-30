from django.db import models


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Carro(models.Model):

    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    ano = models.CharField(max_length=4)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagem = models.IntegerField(default=0)
    conserto = models.IntegerField(default=0)

    def __str__(self):
        return self.carro
