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
    ne = models.CharField(verbose_name="NE",max_length=12)
    tipo = models.IntegerField(choices=CHOICES_TIPO)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='notas')
    requerente = models.CharField(verbose_name="REQUERENTE",max_length=4)
    prazo = models.IntegerField()

    def __str__(self):
        return self.ne


class Pagamento(models.Model):
    ne = models.ForeignKey(NotaEmpenho, on_delete=models.CASCADE, related_name='pagamentos')
    valor_pago = models.FloatField(verbose_name='valor')
    data = models.DateField(verbose_name='data',auto_now="true")
    nfe = models.IntegerField(verbose_name='nota fiscal')
    processo = models.CharField(verbose_name='processo',max_length=20)

    def __str__(self):
        return "{0}".format(self.processo)

