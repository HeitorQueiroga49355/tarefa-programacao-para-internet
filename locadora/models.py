from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nome

class Locacao(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    data = models.DateField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.cliente.nome

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self): return self.nome

class Filme(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=255)
    valor = models.FloatField()
    categoria = models.ManyToManyField(Categoria)

    def __str__(self): return self.titulo


