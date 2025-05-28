
from django.urls import path,include
from . import views

urlpatterns = [
    path('atendidos_json/', views.atendidos_por_atendente_json, name='atendidos_por_atendente_json'),
    path('bazares_json/', views.bazares_json, name='bazares_json'),
    path('doacoes_json/', views.doacoes_json, name='doacoes_json'),
    path('doacoes_pizza_json/', views.doacoes_pizza_json, name='doacoes_pizza_json'),
    path('refugiados_json_sexo/', views.refugiados_json_sexo, name='refugiados_json_sexo'),
    path('refugiados_json_paises/', views.refugiados_json_paises, name='refugiados_json_paises'),
    path('refugiados_json_medicamentos/', views.refugiados_json_medicamentos, name='refugiados_json_medicamentos'),
    path('refugiados_json_trabalha/', views.refugiados_json_trabalha, name='refugiados_json_trabalha'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard_view, name='dashboard'),
    path('bazar/', views.bazar_view, name='bazar'),
    path('bazar/editar/<int:id_bazar>', views.editar_bazar_view, name='editar_bazar'),   
    path('bazar/deletar/<int:id_bazar>', views.deletar_bazar_view, name='deletar_bazar'),
    path('doacao/', views.doacao_view, name='doacao'),
    path('doacao/editar/<int:id_doacao>', views.editar_doacao_view, name='editar_doacao'),   
    path('doacao/deletar/<int:id_doacao>', views.deletar_doacao_view, name='deletar_doacao'),
    path('refugiado/', views.refugiado_view, name='refugiado'),
    path('refugiado/editar/<int:id_refugiado>', views.editar_refugiado_view, name='editar_refugiado'),   
    path('refugiado/deletar/<int:id_refugiado>', views.deletar_refugiado_view, name='deletar_refugiado'),
    path('refugiado/<int:refugiado_id>/', views.detalhes_refugiado, name='detalhes_refugiado'),
    path('refugiado/<int:refugiado_id>/adicionar_filho/', views.adicionar_filho, name='adicionar_filho'),
    path('config/', views.config_view, name='config'),
    path('config/editar_tipo_docao/<int:id_tipo_doacao>', views.editar_tipo_doacao_view, name='editar_tipo_doacao'),   
    path('config/deletar_tipo_doacao/<int:id_tipo_doacao>', views.deletar_tipo_doacao_view, name='deletar_tipo_doacao'),
    path('config/editar_tipo_doc/<int:id_tipo_doc>', views.editar_tipo_doc_view, name='editar_tipo_doc'),   
    path('config/deletar_tipo_doc/<int:id_tipo_doc>', views.deletar_tipo_doc_view, name='deletar_tipo_doc'),
    path('config/editar_tipo_residencia/<int:id_tipo_residencia>', views.editar_tipo_residencia_view, name='editar_tipo_residencia'),   
    path('config/deletar_tipo_residencia/<int:id_tipo_residencia>', views.deletar_tipo_residencia_view, name='deletar_tipo_residencia'),
    path('config/editar_profissao/<int:id_profissao>', views.editar_profissao_view, name='editar_profissao'),   
    path('config/deletar_profissao/<int:id_profissao>', views.deletar_profissao_view, name='deletar_profissao'),
    path('config/editar_colegio/<int:id_colegio>', views.editar_colegio_view, name='editar_colegio'),   
    path('config/deletar_colegio/<int:id_colegio>', views.deletar_colegio_view, name='deletar_colegio'),
    path('config/editar_religiao/<int:id_religiao>', views.editar_religiao_view, name='editar_religiao'),   
    path('config/deletar_religiao/<int:id_religiao>', views.deletar_religiao_view, name='deletar_religiao'),
    path('config/editar_escolaridade/<int:id_escolaridade>', views.editar_escolaridade_view, name='editar_escolaridade'),   
    path('config/deletar_escolaridade/<int:id_escolaridade>', views.deletar_escolaridade_view, name='deletar_escolaridade'),
    path('config/editar_medicamento/<int:id_medicamento>', views.editar_medicamento_view, name='editar_medicamento'),   
    path('config/deletar_medicamento/<int:id_medicamento>', views.deletar_medicamento_view, name='deletar_medicamento'),
    path('config/editar_GrauParDoParNoPais/<int:id_GrauParDoParNoPais>', views.editar_GrauParDoParNoPais_view, name='editar_GrauParDoParNoPais'),   
    path('config/deletar_GrauParDoParNoPais/<int:id_GrauParDoParNoPais>', views.deletar_GrauParDoParNoPais_view, name='deletar_GrauParDoParNoPais'),
    path('config/editar_LocalAtendimento/<int:id_LocalAtendimento>', views.editar_LocalAtendimento_view, name='editar_LocalAtendimento'),   
    path('config/deletar_LocalAtendimento/<int:id_LocalAtendimento>', views.deletar_LocalAtendimento_view, name='deletar_LocalAtendimento'),
    path('refugiado/excluir/<int:documento_id>/<int:refugiado_id>', views.excluir_documento, name='excluir_documento'),


   

  
]