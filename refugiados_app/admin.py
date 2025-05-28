from django.contrib import admin
from .models import Bazar,Doacao,TipoDoacao,Refugiado,TipoDoc,TipoResidencia,Profissao,Filho,Atendido,DocumentosArquivoDigital,User,Atendente
# Register your models here.
admin.site.register(Bazar)
admin.site.register(Doacao)
admin.site.register(TipoDoacao)
admin.site.register(Refugiado)
admin.site.register(TipoDoc)
admin.site.register(TipoResidencia)
admin.site.register(Profissao)
admin.site.register(Filho)
admin.site.register(Atendido)
admin.site.register(DocumentosArquivoDigital)
admin.site.register(Atendente)