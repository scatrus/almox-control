from django.db import models
from localflavor.br.models import BRCNPJField, BRStateField

CHOICES_TIPO = (
    (1, "Ordinário"),
    (2, "Global"),
    (3, "Estimativa")
    )

class Fornecedor(models.Model):
    cnpj = BRCNPJField(verbose_name='CNPJ', max_length=14)
    razao = models.CharField(verbose_name="Razão Social", max_length=100)
    estado = BRStateField(verbose_name="Estado")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(verbose_name="Telefone", max_length=15)

    def __str__(self):
        return "{0}".format(self.razao)


class NotaEmpenho(models.Model):
    ne = models.CharField(verbose_name='NE', max_length=16)
    data = models.DateField(verbose_name='Data', auto_now_add=True)
    valor = models.FloatField(verbose_name='Valor')
    saldo = models.FloatField(verbose_name='Saldo')
    descricao = models.CharField(verbose_name='Descrição', max_length=16)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='notas')
    tipo = models.IntegerField(choices=CHOICES_TIPO)
    requerente = models.CharField(verbose_name='Requerente', max_length=4)
    observacao = models.CharField(verbose_name='Observacao', max_length=255)
    prazoEntrega = models.CharField(verbose_name='PrazoEntrega', max_length=20)

    def __str__(self):
        return self.ne

class Pagamento(models.Model):
    ne = models.ForeignKey(NotaEmpenho, on_delete=models.CASCADE)
    valorPago = models.FloatField(verbose_name='ValorPago')
    dataPagamento = models.DateField(verbose_name='DataPag', auto_now_add=True)
    notaFiscal = models.IntegerField(verbose_name='NotaFiscal') 
    credor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='pagamentos')
    processo = models.CharField(verbose_name='Processo', max_length=20)

    def __str__(self):
        return "{0}".format(self.processo)