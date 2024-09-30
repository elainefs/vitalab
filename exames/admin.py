from django.contrib import admin
from .models import TiposExame, SolicitacaoExame, PedidosExame, AcessoMedico

admin.site.register(TiposExame)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidosExame)
admin.site.register(AcessoMedico)