from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome',
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name= 'Sobrenome',
    )

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail', 
        unique = True,
    )
    senha = models.CharField(
        max_length = 10,
        verbose_name = 'Senha',
    )

    def __str__(self):
        return (f'{self.nome} + {self.sobrenome}')