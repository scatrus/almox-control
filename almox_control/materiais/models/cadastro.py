from django.db import models
from localflavor.br.models import BRCNPJField, BRStateField

CHOICES_TIPO = (
    (1, "Ordinário"),
    (2, "Global"),
    (3, "Estimativa")
    )

class Fornecedor(models.Model):
    cnpj = BRCNPJField(verbose_name="CNPJ")
    razao = models.CharField(verbose_name="Razão Social", max_length=100)
    estado = BRStateField(verbose_name="Estado")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(verbose_name="Telefone", max_length=15)

    def __str__(self):
        return "{0}".format(self.cnpj)


class NotaEmpenho(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='notas')

    tipo = models.IntegerField(choices=CHOICES_TIPO)
