from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bazar,Doacao,Refugiado,TipoDoc,TipoDoacao,TipoResidencia,Profissao,Colegio,Filho,Religiao,Escolaridade,Medicamento,Utiliza,GrauParDoParNoPais,Tem,LocalAtendimento,DocumentosArquivoDigital,Atendente,Atendido
from .forms  import BazarForm,DoacaoForm,RefugiadoForm,TipoDocForm,TipoDoacaoForm,TipoResidenciaForm,ProfissaoForm,ColegioForm,FilhoForm,ReligiaoForm,EscolaridadeForm,MedicamentoForm,GrauParDoParNoPaisForm,LocalAtendimentoForm,DocumentosArquivoDigitalForm,UserRegisterForm,AtendenteForm
import json
from datetime import datetime
from django.core.serializers import serialize
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models import Count


def atendidos_por_atendente_json(request):
    # Agrupa os dados pelo atendente e conta os refugiados atendidos
    dados_atendentes = (
        Atendido.objects.values('fk_atendente__nome')
        .annotate(numero_refugiados=Count('fk_refugiado', distinct=True))
        .order_by('-numero_refugiados')  # Ordena por número de refugiados, do maior para o menor
    )

    # Cria a estrutura de resposta no formato esperado
    response_data = [
        {
            'atendente': item['fk_atendente__nome'],
            'numero_refugiados': item['numero_refugiados']
        }
        for item in dados_atendentes
    ]

    return JsonResponse(response_data, safe=False)

    
def refugiados_json_trabalha(request):
    # Contar a quantidade de refugiados por medicamento usando a tabela intermediária 'Utiliza'
    trabalham = Refugiado.objects.filter(trabalha=True).values('trabalha').annotate(qtd_refugiados=Count('trabalha'))
    nao_trabalham  = Refugiado.objects.filter(trabalha=False).values('trabalha').annotate(qtd_refugiados=Count('trabalha'))
    quantidade_trabalham = [d['qtd_refugiados'] for d in trabalham]
    quantidade_nao_trabalham = [d['qtd_refugiados'] for d in nao_trabalham] or 0

    
    # Organizar a resposta para o JSON
    response_data = {
        'quantidade_trabalham': quantidade_trabalham,
        'quantidade_nao_trabalham':quantidade_nao_trabalham
    }
    
    return JsonResponse(response_data, safe=False)



def refugiados_json_medicamentos(request):
    # Contar a quantidade de refugiados por medicamento usando a tabela intermediária 'Utiliza'
    dados = Refugiado.objects.values('medicamentos__nome').annotate(qtd_refugiados=Count('medicamentos'))
    
    # Filtrar dados para remover valores inválidos
    medicamentos = [d['medicamentos__nome'] for d in dados if d['medicamentos__nome'] not in (None, '')]
    quantidades = [d['qtd_refugiados'] for d in dados if d['medicamentos__nome'] not in (None, '')]
    
    # Garantir que ambos os arrays sejam consistentes
    if not medicamentos:
        medicamentos = ['Nenhum medicamento']
        quantidades = [0]

    # Organizar a resposta para o JSON
    response_data = {
        'labels_medicamentos': medicamentos,
        'quantidade_por_medicamentos': quantidades
    }
    
    return JsonResponse(response_data, safe=False)


def refugiados_json_paises(request):
    dados = Refugiado.objects.values('nacionalidade').annotate(qtd_refugiados=Count('id'))
    nacionalidades = [d['nacionalidade'] for d in dados]
    quantidades = [d['qtd_refugiados'] for d in dados]
    
    response_data = {

      'labels_nacionalidades':nacionalidades,
      'quantidade_por_paises':quantidades
    }
    
    return JsonResponse(response_data, safe=False)


def refugiados_json_sexo(request):
    num_refugiados_masculino = Refugiado.objects.all().filter(sexo='Masculino').count()
    num_refugiados_feminino = Refugiado.objects.all().filter(sexo='Feminino').count()
    num_refugiados_outro = Refugiado.objects.all().filter(sexo='Outro').count()
    
    # dados = Refugiado.objects.values('nacionalidade').annotate(qtd_refugiados=Count('id'))
    # nacionalidades = [d['nacionalidade'] for d in dados]
    # quantidades = [d['qtd_refugiados'] for d in dados]

    response_data = {
      'numero_refugiados_sexo':[num_refugiados_feminino,num_refugiados_masculino,num_refugiados_outro],
      'labels':['Feminino','Masculino','Outro'],
    #   'labels_nacionalidades':nacionalidades,
    #   'quantidade_por_paises':quantidades
    }
    
    return JsonResponse(response_data, safe=False)


def bazares_json(request):
    bazares = Bazar.objects.all()
    bazares_serialized = serialize('json', bazares)
    bazares_data = json.loads(bazares_serialized)  # Converte JSON string em objeto Python
    return JsonResponse(bazares_data, safe=False)  # safe=False permite listas


def doacoes_pizza_json(request):
    # Agrupando as doações por tipo de doação (Recebida, Efetuada)
    doacoes_agrupadas = Doacao.objects.values('fk_tipo_doacao__nome').annotate(
        soma_custo=Sum('custo')
    )
    
    response_data = {
        'somas_por_tipo': list(doacoes_agrupadas)  # Retorna a lista de somas por tipo
    }
    
    return JsonResponse(response_data, safe=False)

def doacoes_json(request):
    # Consultando as doações detalhadas
    doacoes = Doacao.objects.select_related('fk_tipo_doacao').all()  # Otimiza consultas relacionadas
    
    # Usando `values` para incluir campos de tabelas relacionadas
    doacoes_data = list(doacoes.values(
        'nome',
        'id',
        'custo',
        'data',
        'fk_tipo_doacao__nome',  # Inclui o nome do tipo de doação (campo relacionado)
        'fk_tipo_doacao'  # ID do tipo de doação
    ))
    
    return JsonResponse(doacoes_data, safe=False)  # safe=False permite listas
@login_required
def excluir_documento(request, documento_id,refugiado_id):
    documento = get_object_or_404(DocumentosArquivoDigital, id=documento_id)
    documento.delete()
    
    return redirect('detalhes_refugiado',refugiado_id)  

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        atendente_form = AtendenteForm(request.POST)
        if user_form.is_valid() and atendente_form.is_valid():
            # Salva o usuário
            user = user_form.save()
            
            # Cria o atendente associado ao usuário
            atendente = atendente_form.save(commit=False)
            atendente.user = user
            atendente.save()
            
            messages.success(request, f"Usuário {user.username} e atendente criados com sucesso!")
            return redirect('login')  # Redirecione para a página de login
        else:
            print(user_form.errors)
            print(atendente_form.errors)
            # Adiciona mensagens de erro do formulário de usuário
            for field, errors in user_form.errors.items():
                for error in errors:
                    if field == "password2":
                        field = "Confirmar Senha"
                    if field == "password1":
                        field == "Senha"
                    if error == "This field is required.":
                        error = "Este campo é obrigatório."
                        
                    if error == "This password is too short. It must contain at least 8 characters.":
                        error = "Esta senha é muito curta. Deve conter pelo menos 8 caracteres"
                        
                    if error == "This password is too common.":
                        error = "Esta senha é muito comum."
                        
                    if error == "This password is entirely numeric.":
                        error = "Esta senha é inteiramente numérica."              
                    messages.error(request, f"Erro no campo {field}: {error}")
            
            # Adiciona mensagens de erro do formulário de atendente
            for field, errors in atendente_form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")
    else:
        user_form = UserRegisterForm()
        atendente_form = AtendenteForm()
    
    return render(request, 'register.html', {
        'user_form': user_form,
        'atendente_form': atendente_form
    })
    

def adicionar_filho(request, refugiado_id):
    refugiado = get_object_or_404(Refugiado, id=refugiado_id)

    if request.method == 'POST':
        form = FilhoForm(request.POST)
        if form.is_valid():
            filho = form.save(commit=False)
            filho.fk_refugiado = refugiado  # Associa o filho ao refugiado
            filho.save()
            return redirect('detalhes_refugiado', refugiado_id=refugiado.id)  # Redireciona para a página de detalhes do refugiado
    else:
        form = FilhoForm()

    return render(request, 'adicionar_filho.html', {'form': form, 'refugiado': refugiado})

def detalhes_refugiado(request, refugiado_id):
    refugiado = get_object_or_404(Refugiado, id=refugiado_id)
    filhos = Filho.objects.filter(fk_refugiado=refugiado)  
    quantidade_filhos = Filho.objects.filter(fk_refugiado=refugiado).count()
    graus_parentesco = GrauParDoParNoPais.objects.filter(tem__fk_refugiado=refugiado)
    localAtendimento_lista = LocalAtendimento.objects.filter(atendido__fk_refugiado=refugiado)
    arquivos = DocumentosArquivoDigital.objects.filter(fk_refugiado = refugiado)
    
    return render(request, 'detalhes_refugiado.html', {'refugiado': refugiado, 'filhos': filhos, 'graus_parentesco': graus_parentesco,'localAtendimento_lista':localAtendimento_lista,'arquivos':arquivos,'quantidade_filhos':quantidade_filhos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Tenta pegar o atendente relacionado ao usuário
    try:
        atendente = request.user.atendente
    except Atendente.DoesNotExist:
        # Se não houver um atendente, cria um novo
        atendente = Atendente.objects.create(user=request.user, nome=request.user.username, nacionalidade="Brasileiro", rg=0, cpf=0, nascimento="1999-01-09", endereco="", grupo="Gerente")

    return render(request, 'dashboard.html', {'atendente': atendente})

def bazar_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = BazarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bazar')  # Adicione o 'return' aqui para garantir o redirecionamento
        else:
            print(form.errors)
            messages.error(request, 'Erro ao salvar o bazar')

    form = BazarForm()
    bazares = Bazar.objects.all().order_by('id')

    labels = [bazar.titulo for bazar in bazares ]
    data = [ bazar.valorTotal for bazar in bazares]

    return render(request, 'bazar.html', {'form': form,'bazares':bazares, 'labels':labels,'data':data})  # Passar o form para o template


def editar_bazar_view(request, id_bazar):
    bazar = get_object_or_404(Bazar, id=id_bazar)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = BazarForm(request.POST, instance=bazar)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('bazar')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = BazarForm(instance=bazar)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_bazar.html', {'form': form})

def deletar_bazar_view(request, id_bazar):
    bazar = get_object_or_404(Bazar, id=id_bazar)  # Obter o Bazar ou retornar 404 se não encontrado
    bazar.delete()  # Deleta o Bazar do banco de dados
    return redirect('bazar')



def doacao_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doacao')  # Adicione o 'return' aqui para garantir o redirecionamento
        else:
            print(form.errors)
            messages.error(request, 'Erro ao salvar a Doação')

    form = DoacaoForm()
    doacoes = Doacao.objects.all().order_by('id')

    

    return render(request, 'doacao.html', {'form': form,'doacoes':doacoes})  # Passar o form para o template



def editar_doacao_view(request, id_doacao):
    doacao = get_object_or_404(Doacao, id=id_doacao)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = DoacaoForm(request.POST, instance=doacao)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('doacao')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = DoacaoForm(instance=doacao)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_doacao.html', {'form': form})

def deletar_doacao_view(request, id_doacao):
    doacao = get_object_or_404(Doacao, id=id_doacao)  # Obter o Bazar ou retornar 404 se não encontrado
    doacao.delete()  # Deleta o Bazar do banco de dados
    return redirect('doacao')

def refugiado_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    medicamentos = Medicamento.objects.all()
    grauParDoParNoPais_lista = GrauParDoParNoPais.objects.all()
    localAtendimento_lista = LocalAtendimento.objects.all()

    if request.method == 'POST':
        form = RefugiadoForm(request.POST)
        form_doc = DocumentosArquivoDigital(request.POST,request.FILES)
        
        if form.is_valid():
            # Salva o refugiado
            refugiado = form.save()
            arquivos = request.FILES.getlist('arquivo')
            for arquivo in arquivos:
                DocumentosArquivoDigital.objects.create(
                    fk_refugiado=refugiado,  # Suponha que 'refugiado' é um objeto já criado
                    arquivo=arquivo  # Atribui o arquivo a cada registro
                )
            medicamentos_selecionados = request.POST.getlist('medicamentos')  # Pega os medicamentos selecionados
            GrauParDoParNoPais_selecionados = request.POST.getlist('GrauParDoParNoPais')  # Pega os medicamentos selecionados
            LocalAtendimento_selecionados = request.POST.getlist('LocalAtendimento')
            
            refugiado.medicamentos.clear()  # Remove medicamentos antigos
            refugiado.GrauParDoParNoPais.clear()  # Remove medicamentos antigos
            refugiado.LocalAtendimento.clear()
            
            for LocalAtendimento_id in LocalAtendimento_selecionados:
                localAtendimento = LocalAtendimento.objects.get(id=LocalAtendimento_id)
                refugiado.LocalAtendimento.add(localAtendimento)  
                
            for medicamento_id in medicamentos_selecionados:
                medicamento = Medicamento.objects.get(id=medicamento_id)
                refugiado.medicamentos.add(medicamento)  # Associa os novos medicament
                
            for GrauParDoParNoPais_id in GrauParDoParNoPais_selecionados:
                grauParDoParNoPais = GrauParDoParNoPais.objects.get(id=GrauParDoParNoPais_id)
                refugiado.GrauParDoParNoPais.add(grauParDoParNoPais)  # Associa os novos medicament   
    
    
            try:
                quantidade_filhos = int(request.POST.get('quantidade_filhos', 0))
            except (TypeError, ValueError):
                quantidade_filhos = 0
            
            for i in range(quantidade_filhos):
                nome = request.POST.get(f'filho_{i}_nome')
                nascimento = request.POST.get(f'filho_{i}_nascimento')
                nacionalidade = request.POST.get(f'filho_{i}_nacionalidade')
                colegio_id = request.POST.get(f'filho_{i}_colegio')
                escolaridade_id = request.POST.get(f'filho_{i}_escolaridade')

                colegio = Colegio.objects.get(id=colegio_id) if colegio_id else None
                escolaridade = Escolaridade.objects.get(id=escolaridade_id) if escolaridade_id else None

                if nome and nascimento and nacionalidade:
                    Filho.objects.create(
                        nome=nome,
                        nascimento=nascimento,
                        nacionalidade=nacionalidade,
                        fk_refugiado=refugiado,
                        fk_colegio=colegio,
                        fk_escolaridade=escolaridade
                    )
            
            atendido = Atendido.objects.create(
            fk_refugiado=refugiado,
            fk_atendente=request.user.atendente  # Atribui o atendente da requisição
        )
            messages.success(request, 'Refugiado e filhos salvos com sucesso!')
            return redirect('refugiado')
        else:
            messages.error(request, 'Erro ao salvar o refugiado')

    form = RefugiadoForm()
    form_doc = RefugiadoForm()
    refugiados = Refugiado.objects.all().order_by('id')
    colegios = list(Colegio.objects.values('id', 'nome'))
    escolaridades = list(Escolaridade.objects.values('id', 'nome'))
    return render(request, 'refugiado.html', {
        'form': form,
        'form_doc': form_doc,
        'refugiados': refugiados,
        'colegios_json': json.dumps(colegios),
        'escolaridades_json': json.dumps(escolaridades),
        'medicamentos': medicamentos,
        'grauParDoParNoPais_lista': grauParDoParNoPais_lista,
        'localAtendimento_lista': localAtendimento_lista
    })
    
    
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Refugiado, Medicamento, GrauParDoParNoPais, LocalAtendimento, Filho, Colegio, Escolaridade, DocumentosArquivoDigital
from .forms import RefugiadoForm

def editar_refugiado_view(request, id_refugiado):
    if not request.user.is_authenticated:
        return redirect('login')

    refugiado = get_object_or_404(Refugiado, id=id_refugiado)
    medicamentos = Medicamento.objects.all()
    grau_parente_lista = GrauParDoParNoPais.objects.all()
    local_atendimento_lista = LocalAtendimento.objects.all()
    filhos = Filho.objects.filter(fk_refugiado=refugiado).select_related('fk_colegio', 'fk_escolaridade')

    if request.method == 'POST':
        form = RefugiadoForm(request.POST, instance=refugiado)
        form_doc = DocumentosArquivoDigital(request.POST, request.FILES)

        if form.is_valid():
            refugiado = form.save()
            arquivos = request.FILES.getlist('arquivo')
            
            # Validação e salvamento de arquivos
            for arquivo in arquivos:
                if arquivo.size > 5 * 1024 * 1024:  # Limite de 5MB
                    messages.error(request, "O arquivo é muito grande.")
                    continue
                if not arquivo.content_type.startswith('application/pdf'):  # Exemplo para PDFs
                    messages.error(request, "Apenas arquivos PDF são permitidos.")
                    continue
                DocumentosArquivoDigital.objects.create(fk_refugiado=refugiado, arquivo=arquivo)
                
            # Tratamento dos medicamentos selecionados
            medicamentos_selecionados = request.POST.getlist('medicamentos')
            for medicamento_id in medicamentos_selecionados:
                try:
                    medicamento = Medicamento.objects.get(id=medicamento_id)
                    refugiado.medicamentos.add(medicamento)
                except Medicamento.DoesNotExist:
                    messages.error(request, f"Medicamento com ID {medicamento_id} não encontrado.")
            
            # Tratamento dos grau de parentesco e local de atendimento
            grau_parente_selecionados = request.POST.getlist('GrauParDoParNoPais')
            local_atendimento_selecionados = request.POST.getlist('LocalAtendimento')
            
            for field, model, selected_ids in [
                ('medicamentos', Medicamento, medicamentos_selecionados),
                ('GrauParDoParNoPais', GrauParDoParNoPais, grau_parente_selecionados),
                ('LocalAtendimento', LocalAtendimento, local_atendimento_selecionados)
            ]:
                getattr(refugiado, field).clear()
                for obj_id in selected_ids:
                    try:
                        obj = model.objects.get(id=obj_id)
                        getattr(refugiado, field).add(obj)
                    except model.DoesNotExist:
                        messages.error(request, f"{model.__name__} com ID {obj_id} não encontrado.")
            
            # Atualizando ou criando filhos
            for i in range(len(filhos)):
                filho_id = request.POST.get(f'filhos[{i}][id]')
                nome = request.POST.get(f'filhos[{i}][nome]')
                nascimento = request.POST.get(f'filhos[{i}][nascimento]')
                escolaridade_id = request.POST.get(f'filhos[{i}][fk_escolaridade]')
                colegio_id = request.POST.get(f'filhos[{i}][fk_colegio]')

                if filho_id:
                    filho = Filho.objects.get(id=filho_id)
                    filho.nome = nome
                    filho.nascimento = nascimento
                    filho.fk_escolaridade_id = escolaridade_id
                    filho.fk_colegio_id = colegio_id
                    filho.save()
                else:
                    Filho.objects.create(
                        fk_refugiado=refugiado,
                        nome=nome,
                        nascimento=nascimento,
                        fk_escolaridade_id=escolaridade_id,
                        fk_colegio_id=colegio_id
                    )
                    
            messages.success(request, 'Refugiado atualizado com sucesso!')
            return redirect('detalhes_refugiado', refugiado_id=id_refugiado)
            print("Formulário válido!")

        else:
            messages.error(request, 'Erro ao salvar. Verifique os dados informados.')
            print("Formulário inválido!")
            print(form.errors)  # Isso mostrará os erros do formulário

    form = RefugiadoForm(instance=refugiado)
    form_doc = RefugiadoForm()
    colegios = Colegio.objects.all()
    escolaridades = Escolaridade.objects.all()
    # Serializando dados para o JavaScript
    colegios_json = serialize('json', colegios)
    escolaridades_json = serialize('json', escolaridades)

    return render(request, 'editar_refugiado.html', {
        'form': form,
        'form_doc': form_doc,
        'refugiado': refugiado,
        'filhos': filhos,
        'colegios': colegios,
        'medicamentos': medicamentos,
        'escolaridades': escolaridades,
        'grau_parente_lista': grau_parente_lista,
        'local_atendimento_lista': local_atendimento_lista,
    })


# def editar_refugiado_view(request, id_refugiado):
#     if not request.user.is_authenticated:
#         return redirect('login')

#     refugiado = get_object_or_404(Refugiado, id=id_refugiado)
#     medicamentos = Medicamento.objects.all()
#     grau_parente_lista = GrauParDoParNoPais.objects.all()
#     local_atendimento_lista = LocalAtendimento.objects.all()
#     filhos = Filho.objects.filter(fk_refugiado=refugiado).select_related('fk_colegio', 'fk_escolaridade')

#     if request.method == 'POST':
#         form = RefugiadoForm(request.POST, instance=refugiado)
#         form_doc = DocumentosArquivoDigital(request.POST,request.FILES)

#         if form.is_valid():
#             refugiado = form.save()
#             arquivos = request.FILES.getlist('arquivo')
#             for arquivo in arquivos:
#                 DocumentosArquivoDigital.objects.create(
#                     fk_refugiado=refugiado,  # Suponha que 'refugiado' é um objeto já criado
#                     arquivo=arquivo  # Atribui o arquivo a cada registro
#                 )
                
#             medicamentos_selecionados = request.POST.getlist('medicamentos')  # Pega os medicamentos selecionados
#             GrauParDoParNoPais_selecionados = request.POST.getlist('GrauParDoParNoPais')  # Pega os medicamentos selecionados
#             LocalAtendimento_selecionados = request.POST.getlist('LocalAtendimento')
            
#             refugiado.medicamentos.clear()  # Remove medicamentos antigos
#             refugiado.GrauParDoParNoPais.clear()  # Remove medicamentos antigos
#             refugiado.LocalAtendimento.clear()
            
#             for LocalAtendimento_id in LocalAtendimento_selecionados:
#                 localAtendimento = LocalAtendimento.objects.get(id=LocalAtendimento_id)
#                 refugiado.LocalAtendimento.add(localAtendimento)  
                
#             for medicamento_id in medicamentos_selecionados:
#                 medicamento = Medicamento.objects.get(id=medicamento_id)
#                 refugiado.medicamentos.add(medicamento)  # Associa os novos medicament
                
#             for GrauParDoParNoPais_id in GrauParDoParNoPais_selecionados:
#                 grauParDoParNoPais = GrauParDoParNoPais.objects.get(id=GrauParDoParNoPais_id)
#                 refugiado.GrauParDoParNoPais.add(grauParDoParNoPais)  # Associa os novos medicament  
                    
#             for i in range(len(filhos)):
#                 filho_id = request.POST.get(f'filhos[{i}][id]')
#                 nome = request.POST.get(f'filhos[{i}][nome]')
#                 nascimento = request.POST.get(f'filhos[{i}][nascimento]')
#                 escolaridade_id = request.POST.get(f'filhos[{i}][fk_escolaridade]')
#                 colegio_id = request.POST.get(f'filhos[{i}][fk_colegio]')

#                 if filho_id:
#                     filho = Filho.objects.get(id=filho_id)
#                     filho.nome = nome
#                     filho.nascimento = nascimento
#                     filho.fk_escolaridade_id = escolaridade_id
#                     filho.fk_colegio_id = colegio_id
#                     filho.save()
                    
#             messages.success(request, 'Refugiado atualizado com sucesso!')
#             return redirect('detalhes_refugiado',refugiado_id=id_refugiado)
#         else:
#             messages.error(request, 'Erro ao salvar. Verifique os dados informados.')
        

#     form = RefugiadoForm(instance=refugiado)
#     form_doc = RefugiadoForm()
#     colegios = Colegio.objects.all()
#     escolaridades = Escolaridade.objects.all()
#     print(local_atendimento_lista)
#     return render(request, 'editar_refugiado.html', {
#         'form': form,
#         'form_doc':form_doc,
#         'refugiado': refugiado,
#         'filhos': filhos,
#         'colegios': colegios,
#         'medicamentos': medicamentos,
#         'escolaridades': escolaridades,
#         'grau_parente_lista': grau_parente_lista,
#         'local_atendimento_lista': local_atendimento_lista,
#     })

def deletar_refugiado_view(request, id_refugiado):
    refugiado = get_object_or_404(Refugiado, id=id_refugiado)  # Obter o Bazar ou retornar 404 se não encontrado
    refugiado.delete()  # Deleta o Bazar do banco de dados
    return redirect('refugiado')


def config_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        if 'submit_tipo_doc' in request.POST:  # Suponha que você usa botões diferentes para os formulários
            form = TipoDocForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')

        elif 'submit_tipo_doacao' in request.POST:
            form = TipoDoacaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')
        elif 'submit_tipo_residencia' in request.POST:
            form = TipoResidenciaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')

        elif 'submit_profissao' in request.POST:
            form = ProfissaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')

        elif 'submit_colegio' in request.POST:
            form = ColegioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')

        elif 'submit_religiao' in request.POST:
            form = ReligiaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')    
                    
        elif 'submit_escolaridade' in request.POST:
            form = EscolaridadeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')
        
        elif 'submit_medicamento' in request.POST:
            form = MedicamentoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')
                
        elif 'submit_GrauParDoParNoPais' in request.POST:
            form = GrauParDoParNoPaisForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')   
        
        elif 'submit_LocalAtendimento' in request.POST:
            form = LocalAtendimentoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')
                
        elif 'submit_register_atendente' in request.POST:
            
            user_form = UserRegisterForm(request.POST)
            atendente_form = AtendenteForm(request.POST)
            
            if user_form.is_valid() and atendente_form.is_valid():
                # Salva o usuário
                user = user_form.save()
                # Cria o atendente associado ao usuário
                atendente = atendente_form.save(commit=False)
                atendente.user = user
                atendente.save()
                messages.success(request, f"Usuário {user.username} e atendente criados com sucesso!")
                return redirect('config')  # Adicione o 'return' aqui para garantir o redirecionamento
            else:
                print(form.errors)
                messages.error(request, 'Erro ao salvar')              
                                 
                     
    form_medicamento = MedicamentoForm()
    lista_medicamento = Medicamento.objects.all().order_by('id')
    
    form_LocalAtendimento = LocalAtendimentoForm()
    lista_LocalAtendimento = LocalAtendimento.objects.all().order_by('id')
    
    form_GrauParDoParNoPais = GrauParDoParNoPaisForm()
    lista_GrauParDoParNoPais = GrauParDoParNoPais.objects.all().order_by('id')
    
    form_religiao = ReligiaoForm()
    lista_religiao = Religiao.objects.all().order_by('id')
    
    form_escolaridade = EscolaridadeForm()
    lista_escolaridade = Escolaridade.objects.all().order_by('id')
    
    form_tipo_doc = TipoDocForm()
    tiposDoc = TipoDoc.objects.all().order_by('id')

    form_tipo_doacao = TipoDoacaoForm()
    tiposDoacao = TipoDoacao.objects.all().order_by('id')

    form_tipo_residencia = TipoResidenciaForm()
    tiposResidencia = TipoResidencia.objects.all().order_by('id')

    form_profissao = ProfissaoForm()
    lista_profissao = Profissao.objects.all().order_by('id')

    form_colegio = ColegioForm()
    lista_colegio = Colegio.objects.all().order_by('id')

    context = {'form_tipo_doc':form_tipo_doc,
               'form_tipo_doacao':form_tipo_doacao,
               'form_tipo_residencia':form_tipo_residencia,
               'tipos_doc':tiposDoc,
               'tipos_doacao':tiposDoacao,
               'tipos_residencia':tiposResidencia,
               'form_profissao':form_profissao,
               'lista_profissao':lista_profissao,
               'form_colegio':form_colegio,
               'lista_colegio':lista_colegio,
               'form_religiao':form_religiao,
               'lista_religiao':lista_religiao,
               'form_escolaridade':form_escolaridade,
               'lista_escolaridade':lista_escolaridade,
               'form_medicamento':form_medicamento,
               'lista_medicamento':lista_medicamento,
               'form_GrauParDoParNoPais':form_GrauParDoParNoPais,
               'lista_GrauParDoParNoPais':lista_GrauParDoParNoPais,
               'form_LocalAtendimento':form_LocalAtendimento,
               'lista_LocalAtendimento':lista_LocalAtendimento
               
               }
    
    return render(request, 'config.html',context)  




def editar_tipo_doacao_view(request, id_tipo_doacao):
    tipo_doacao = get_object_or_404(TipoDoacao, id=id_tipo_doacao)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = TipoDoacaoForm(request.POST, instance=tipo_doacao)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = TipoDoacaoForm(instance=tipo_doacao)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_tipo_doacao.html', {'form': form})

def deletar_tipo_doacao_view(request, id_tipo_doacao):
    tipo_doacao = get_object_or_404(TipoDoacao, id=id_tipo_doacao)  # Obter o Bazar ou retornar 404 se não encontrado
    tipo_doacao.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')

def editar_medicamento_view(request, id_medicamento):
    medicamento = get_object_or_404(Medicamento, id=id_medicamento)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = MedicamentoForm(instance=medicamento)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_medicamento.html', {'form': form})

def deletar_medicamento_view(request, id_medicamento):
    medicamento = get_object_or_404(Medicamento, id=id_medicamento)  # Obter o Bazar ou retornar 404 se não encontrado
    medicamento.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')



def editar_tipo_doc_view(request, id_tipo_doc):
    tipo_doc = get_object_or_404(TipoDoc, id=id_tipo_doc)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = TipoDocForm(request.POST, instance=tipo_doc)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = TipoDocForm(instance=tipo_doc)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_tipo_doc.html', {'form': form})

def deletar_tipo_doc_view(request, id_tipo_doc):
    tipo_doc = get_object_or_404(TipoDoc, id=id_tipo_doc)  # Obter o Bazar ou retornar 404 se não encontrado
    tipo_doc.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')


def editar_tipo_residencia_view(request, id_tipo_residencia):
    tipo_residencia = get_object_or_404(TipoResidencia, id=id_tipo_residencia)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = TipoResidenciaForm(request.POST, instance=tipo_residencia)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = TipoResidenciaForm(instance=tipo_residencia)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_tipo_residencia.html', {'form': form})

def deletar_tipo_residencia_view(request, id_tipo_residencia):
    tipo_residencia = get_object_or_404(TipoResidencia, id=id_tipo_residencia)  # Obter o Bazar ou retornar 404 se não encontrado
    tipo_residencia.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')





def editar_profissao_view(request, id_profissao):
    profissao = get_object_or_404(Profissao, id=id_profissao)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = ProfissaoForm(request.POST, instance=profissao)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = ProfissaoForm(instance=profissao)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_profissao.html', {'form': form})

def deletar_profissao_view(request, id_profissao):
    profissao = get_object_or_404(Profissao, id=id_profissao)  # Obter o Bazar ou retornar 404 se não encontrado
    profissao.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')


def editar_colegio_view(request, id_colegio):
    colegio = get_object_or_404(Colegio, id=id_colegio)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = ColegioForm(request.POST, instance=colegio)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = ColegioForm(instance=colegio)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_colegio.html', {'form': form})

def deletar_colegio_view(request, id_colegio):
    colegio = get_object_or_404(Colegio, id=id_colegio)  # Obter o Bazar ou retornar 404 se não encontrado
    colegio.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')



def editar_religiao_view(request, id_religiao):
    religiao = get_object_or_404(Religiao, id=id_religiao)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = ReligiaoForm(request.POST, instance=religiao)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = ReligiaoForm(instance=religiao)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_religiao.html', {'form': form})

def deletar_religiao_view(request, id_religiao):
    religiao = get_object_or_404(Religiao, id=id_religiao)  # Obter o Bazar ou retornar 404 se não encontrado
    religiao.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')


def editar_escolaridade_view(request, id_escolaridade):
    escolaridade = get_object_or_404(Escolaridade, id=id_escolaridade)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = EscolaridadeForm(request.POST, instance=escolaridade)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = ReligiaoForm(instance=escolaridade)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_escolaridade.html', {'form': form})

def deletar_escolaridade_view(request, id_escolaridade):
    escolaridade = get_object_or_404(Escolaridade, id=id_escolaridade)  # Obter o Bazar ou retornar 404 se não encontrado
    escolaridade.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')

def editar_GrauParDoParNoPais_view(request, id_GrauParDoParNoPais):
    grauParDoParNoPais = get_object_or_404(GrauParDoParNoPais, id=id_GrauParDoParNoPais)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = GrauParDoParNoPaisForm(request.POST, instance=grauParDoParNoPais)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = GrauParDoParNoPaisForm(instance=grauParDoParNoPais)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_GrauParDoParNoPais.html', {'form': form})

def deletar_GrauParDoParNoPais_view(request, id_GrauParDoParNoPais):
    grauParDoParNoPais = get_object_or_404(GrauParDoParNoPais, id=id_GrauParDoParNoPais)  # Obter o Bazar ou retornar 404 se não encontrado
    grauParDoParNoPais.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')


def editar_LocalAtendimento_view(request, id_LocalAtendimento):
    localAtendimento = get_object_or_404(LocalAtendimento, id=id_LocalAtendimento)  # Obter o Bazar ou retornar 404 se não encontrado

    if request.method == 'POST':
        form = LocalAtendimentoForm(request.POST, instance=localAtendimento)  # Passa os dados do POST e a instância existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no banco de dados
            return redirect('config')  # Redireciona para uma página de listagem ou sucesso após salvar
    else:
        form = LocalAtendimentoForm(instance=localAtendimento)  # Se não for POST, preenche o formulário com a instância existente

    return render(request, 'editar_LocalAtendimento.html', {'form': form})

def deletar_LocalAtendimento_view(request, id_LocalAtendimento):
    localAtendimento = get_object_or_404(LocalAtendimento, id=id_LocalAtendimento)  # Obter o Bazar ou retornar 404 se não encontrado
    localAtendimento.delete()  # Deleta o Bazar do banco de dados
    return redirect('config')