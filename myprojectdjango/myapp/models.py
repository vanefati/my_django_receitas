from django.db import models

# Create your models here.

class Receitas(models.Model):

    class Meta:

       db_table = 'receitas'

    titulo = models.CharField(max_length=200)
    tipo_de_culinaria = models.CharField(max_length=200)
    tempo_de_preparo = models.IntegerField()
    quantidade_ingredientes = models.CharField(max_length=200)
    modo_de_preparo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

# class Ingredientes(models.Model):

#     class Meta:

#        db_table = 'receitas'

#     titulo = models.CharField(max_length=200)
#     tipo_de_culinaria = models.CharField(max_length=200)
#     tempo_de_preparo = models.IntegerField()
#     quantidade_ingredientes = models.CharField(max_length=200)
#     modo_de_ preparo = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title