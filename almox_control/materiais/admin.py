from django.contrib import admin
from materiais.models.cadastro import Fornecedor, NotaEmpenho, Pagamento


class FornecedorAdmin(admin.ModelAdmin):
    model = Fornecedor
    list_display = ['cnpj','razao', 'estado', 'email',
                    'telefone']
    list_filter = ['razao', 'estado']
    search_fields = ['razao']

admin.site.register(Fornecedor, FornecedorAdmin)


class NotaEmpenhoAdmin(admin.ModelAdmin):
    model = NotaEmpenho
    list_display = ['ne','data', 'fornecedor', 'tipo']
    list_filter = ['ne', 'data', 'fornecedor']
    search_fields = ['data', 'ne', 'fornecedor']

admin.site.register(NotaEmpenho, NotaEmpenhoAdmin)

class PagamentoAdmin(admin.ModelAdmin):
    model = Pagamento
    list_display = ['ne','valorPago', 'dataPagamento', 'notaFiscal', 'credor', 'processo']
    list_filter = ['ne', 'dataPagamento', 'processo']
    search_fields = ['ne', 'processo']

admin.site.register(Pagamento, PagamentoAdmin)
