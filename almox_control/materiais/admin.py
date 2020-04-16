from django.contrib import admin

from materiais.models.cadastro import Fornecedor, NotaEmpenho, Pagamento

admin.site.register(Fornecedor)
admin.site.register(NotaEmpenho)
admin.site.register(Pagamento)