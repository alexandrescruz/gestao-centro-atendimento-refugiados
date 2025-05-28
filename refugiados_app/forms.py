from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bazar,Doacao,Refugiado,TipoDoc,TipoDoacao,TipoResidencia,Profissao,Colegio,Filho,Religiao,Escolaridade,Medicamento,GrauParDoParNoPais,LocalAtendimento,DocumentosArquivoDigital,Atendente

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Rótulos traduzidos
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2':'Confirmar Senha',
        }
        # Mensagens de erro personalizadas
        error_messages = {
            'username': {
                'required': 'O nome de usuário é obrigatório.',
                'unique': 'Este nome de usuário já está em uso. Escolha outro.',
            },
            'email': {
                'required': 'O e-mail é obrigatório.',
                'invalid': 'Digite um endereço de e-mail válido.',
            },
            'password1': {
                'required': 'O campo senha é obrigatório.',
            },
            'password2': {
                'required': 'O campo confirmar senha é obrigatório.',
                'password_mismatch': 'As senhas não coincidem.',
            },
        }


  
        
        

# Formulário para registrar os dados do atendente
class AtendenteForm(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = ['nome', 'nacionalidade', 'rg', 'cpf', 'nascimento', 'endereco', 'grupo']

        labels = {
            'nome': 'Nome Completo do Atendente',
            'nacionalidade': 'Nacionalidade',
            'rg': 'Rg',
            'cpf': 'Cpf',
            'nascimento': 'Data de Nascimento',
            'endereco': 'Endereço',
            'grupo': 'Grupo',
        }

        choices_paises = [
    ('',''),
    ('Afeganistão', 'Afeganistão'),
    ('África do Sul', 'África do Sul'),
    ('Albânia', 'Albânia'),
    ('Algéria', 'Algéria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antígua e Barbuda', 'Antígua e Barbuda'),
    ('Arábia Saudita', 'Arábia Saudita'),
    ('Argélia', 'Argélia'),
    ('Argentina', 'Argentina'),
    ('Armênia', 'Armênia'),
    ('Austrália', 'Austrália'),
    ('Áustria', 'Áustria'),
    ('Azerbaijão', 'Azerbaijão'),
    ('Bahamas', 'Bahamas'),
    ('Bahrein', 'Bahrein'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Bielorrússia', 'Bielorrússia'),
    ('Bélgica', 'Bélgica'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermudas', 'Bermudas'),
    ('Bolívia', 'Bolívia'),
    ('Bósnia e Herzegovina', 'Bósnia e Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brasil', 'Brasil'),
    ('Brunei', 'Brunei'),
    ('Bulgária', 'Bulgária'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Camboja', 'Camboja'),
    ('Camarões', 'Camarões'),
    ('Canadá', 'Canadá'),
    ('Cabo Verde', 'Cabo Verde'),
    ('República Centro-Africana', 'República Centro-Africana'),
    ('Chade', 'Chade'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Chipre', 'Chipre'),
    ('Colômbia', 'Colômbia'),
    ('Comores', 'Comores'),
    ('República Democrática do Congo', 'República Democrática do Congo'),
    ('Congo', 'Congo'),
    ('Costa Rica', 'Costa Rica'),
    ('Croácia', 'Croácia'),
    ('Cuba', 'Cuba'),
    ('Chipre', 'Chipre'),
    ('República Tcheca', 'República Tcheca'),
    ('Dinamarca', 'Dinamarca'),
    ('Djibuti', 'Djibuti'),
    ('Dominica', 'Dominica'),
    ('Egito', 'Egito'),
    ('El Salvador', 'El Salvador'),
    ('Emirados Árabes Unidos', 'Emirados Árabes Unidos'),
    ('Equador', 'Equador'),
    ('Eritreia', 'Eritreia'),
    ('Estônia', 'Estônia'),
    ('Eswatini', 'Eswatini'),
    ('Espanha', 'Espanha'),
    ('Estados Unidos', 'Estados Unidos'),
    ('Eslováquia', 'Eslováquia'),
    ('Eslovênia', 'Eslovênia'),
    ('Etiópia', 'Etiópia'),
    ('Fiji', 'Fiji'),
    ('Filipinas', 'Filipinas'),
    ('Finlândia', 'Finlândia'),
    ('França', 'França'),
    ('Gabão', 'Gabão'),
    ('Gâmbia', 'Gâmbia'),
    ('Gana', 'Gana'),
    ('Geórgia', 'Geórgia'),
    ('Granada', 'Granada'),
    ('Guerra', 'Guerra'),
    ('Guiana', 'Guiana'),
    ('Guiné', 'Guiné'),
    ('Guiné-Bissau', 'Guiné-Bissau'),
    ('Guatemala', 'Guatemala'),
    ('Guiana', 'Guiana'),
    ('Haiti', 'Haiti'),
    ('Holanda', 'Holanda'),
    ('Honduras', 'Honduras'),
    ('Hungria', 'Hungria'),
    ('Iémen', 'Iémen'),
    ('Ilhas Marshall', 'Ilhas Marshall'),
    ('Ilhas Maurício', 'Ilhas Maurício'),
    ('Ilhas Salomão', 'Ilhas Salomão'),
    ('Índia', 'Índia'),
    ('Indonésia', 'Indonésia'),
    ('Irã', 'Irã'),
    ('Iraque', 'Iraque'),
    ('Irlanda', 'Irlanda'),
    ('Islândia', 'Islândia'),
    ('Israel', 'Israel'),
    ('Itália', 'Itália'),
    ('Jamaica', 'Jamaica'),
    ('Japão', 'Japão'),
    ('Jordânia', 'Jordânia'),
    ('Kiribati', 'Kiribati'),
    ('Kuwait', 'Kuwait'),
    ('Laos', 'Laos'),
    ('Lesoto', 'Lesoto'),
    ('Letônia', 'Letônia'),
    ('Líbano', 'Líbano'),
    ('Libéria', 'Libéria'),
    ('Líbia', 'Líbia'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lituânia', 'Lituânia'),
    ('Luxemburgo', 'Luxemburgo'),
    ('Macedônia do Norte', 'Macedônia do Norte'),
    ('Madagascar', 'Madagascar'),
    ('Malásia', 'Malásia'),
    ('Malawi', 'Malawi'),
    ('Maldivas', 'Maldivas'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marrocos', 'Marrocos'),
    ('Mauritânia', 'Mauritânia'),
    ('Maurícias', 'Maurícias'),
    ('México', 'México'),
    ('Mianmar', 'Mianmar'),
    ('Micronésia', 'Micronésia'),
    ('Moçambique', 'Moçambique'),
    ('Moldávia', 'Moldávia'),
    ('Monaco', 'Mônaco'),
    ('Mongólia', 'Mongólia'),
    ('Montenegro', 'Montenegro'),
    ('Namíbia', 'Namíbia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Nicarágua', 'Nicarágua'),
    ('Níger', 'Níger'),
    ('Nigéria', 'Nigéria'),
    ('Noruega', 'Noruega'),
    ('Nova Zelândia', 'Nova Zelândia'),
    ('Níger', 'Níger'),
    ('Paquistão', 'Paquistão'),
    ('Palau', 'Palau'),
    ('Panamá', 'Panamá'),
    ('Papua Nova Guiné', 'Papua Nova Guiné'),
    ('Paraguai', 'Paraguai'),
    ('Peru', 'Peru'),
    ('Polônia', 'Polônia'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Quênia', 'Quênia'),
    ('República Dominicana', 'República Dominicana'),
    ('República do Congo', 'República do Congo'),
    ('Romênia', 'Romênia'),
    ('Ruanda', 'Ruanda'),
    ('Rússia', 'Rússia'),
    ('São Cristóvão e Névis', 'São Cristóvão e Névis'),
    ('São Marino', 'São Marino'),
    ('São Tomé e Príncipe', 'São Tomé e Príncipe'),
    ('Senegal', 'Senegal'),
    ('Serra Leoa', 'Serra Leoa'),
    ('Seychelles', 'Seychelles'),
    ('Singapura', 'Singapura'),
    ('Somália', 'Somália'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudão', 'Sudão'),
    ('Suriname', 'Suriname'),
    ('Suécia', 'Suécia'),
    ('Suíça', 'Suíça'),
    ('Syria', 'Siria'),
    ('Tadjiquistão', 'Tadjiquistão'),
    ('Tailândia', 'Tailândia'),
    ('Tanzânia', 'Tanzânia'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad e Tobago', 'Trinidad e Tobago'),
    ('Tunísia', 'Tunísia'),
    ('Turcomenistão', 'Turcomenistão'),
    ('Turquia', 'Turquia'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ucrânia', 'Ucrânia'),
    ('Uruguai', 'Uruguai'),
    ('Uzbequistão', 'Uzbequistão'),
    ('Vanuatu', 'Vanuatu'),
    ('Vaticano', 'Vaticano'),
    ('Venezuela', 'Venezuela'),
    ('Vietnã', 'Vietnã'),
    ('Zâmbia', 'Zâmbia'),
    ('Zimbábue', 'Zimbábue')
]
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nome do Atendente'
            }),
            'idade': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Idade'
            }),
            'nacionalidade': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nacionalidade',
            }, choices=choices_paises),
            'rg': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Rg',
                'id':'id_rg'
            }),
            'cpf': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Cpf',
                'id':'id_cpf'
            }),
            'nascimento': forms.DateInput(attrs={
                'class': 'form-control form-input',
                'type': 'date',
                'placeholder': 'Data de Nascimento'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Endereço'
            }),
            'grupo': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Selecione o Grupo'
            }),
        }
        
        
class DocumentosArquivoDigitalForm(forms.ModelForm):
    class Meta:
        model = DocumentosArquivoDigital
        fields = ['arquivo']
        widgets = {
            'arquivo': forms.ClearableFileInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Escolha o arquivo',   # Placeholder para orientação
            }),
          
        }
        
class EscolaridadeForm(forms.ModelForm):
    class Meta:
        model = Escolaridade
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Escolaridade'
            }),
          
        }
        
class FilhoForm(forms.ModelForm):
    class Meta:
        model = Filho
        fields = ['nome', 'nascimento', 'nacionalidade','fk_escolaridade','fk_colegio']
        labels = {
            'fk_escolaridade':'Escolaridade',
            'fk_colegio':'Colégio'
        }
        choices_paises = [
    ('',''),
    ('Afeganistão', 'Afeganistão'),
    ('África do Sul', 'África do Sul'),
    ('Albânia', 'Albânia'),
    ('Algéria', 'Algéria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antígua e Barbuda', 'Antígua e Barbuda'),
    ('Arábia Saudita', 'Arábia Saudita'),
    ('Argélia', 'Argélia'),
    ('Argentina', 'Argentina'),
    ('Armênia', 'Armênia'),
    ('Austrália', 'Austrália'),
    ('Áustria', 'Áustria'),
    ('Azerbaijão', 'Azerbaijão'),
    ('Bahamas', 'Bahamas'),
    ('Bahrein', 'Bahrein'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Bielorrússia', 'Bielorrússia'),
    ('Bélgica', 'Bélgica'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermudas', 'Bermudas'),
    ('Bolívia', 'Bolívia'),
    ('Bósnia e Herzegovina', 'Bósnia e Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brasil', 'Brasil'),
    ('Brunei', 'Brunei'),
    ('Bulgária', 'Bulgária'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Camboja', 'Camboja'),
    ('Camarões', 'Camarões'),
    ('Canadá', 'Canadá'),
    ('Cabo Verde', 'Cabo Verde'),
    ('República Centro-Africana', 'República Centro-Africana'),
    ('Chade', 'Chade'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Chipre', 'Chipre'),
    ('Colômbia', 'Colômbia'),
    ('Comores', 'Comores'),
    ('República Democrática do Congo', 'República Democrática do Congo'),
    ('Congo', 'Congo'),
    ('Costa Rica', 'Costa Rica'),
    ('Croácia', 'Croácia'),
    ('Cuba', 'Cuba'),
    ('Chipre', 'Chipre'),
    ('República Tcheca', 'República Tcheca'),
    ('Dinamarca', 'Dinamarca'),
    ('Djibuti', 'Djibuti'),
    ('Dominica', 'Dominica'),
    ('Egito', 'Egito'),
    ('El Salvador', 'El Salvador'),
    ('Emirados Árabes Unidos', 'Emirados Árabes Unidos'),
    ('Equador', 'Equador'),
    ('Eritreia', 'Eritreia'),
    ('Estônia', 'Estônia'),
    ('Eswatini', 'Eswatini'),
    ('Espanha', 'Espanha'),
    ('Estados Unidos', 'Estados Unidos'),
    ('Eslováquia', 'Eslováquia'),
    ('Eslovênia', 'Eslovênia'),
    ('Etiópia', 'Etiópia'),
    ('Fiji', 'Fiji'),
    ('Filipinas', 'Filipinas'),
    ('Finlândia', 'Finlândia'),
    ('França', 'França'),
    ('Gabão', 'Gabão'),
    ('Gâmbia', 'Gâmbia'),
    ('Gana', 'Gana'),
    ('Geórgia', 'Geórgia'),
    ('Granada', 'Granada'),
    ('Guerra', 'Guerra'),
    ('Guiana', 'Guiana'),
    ('Guiné', 'Guiné'),
    ('Guiné-Bissau', 'Guiné-Bissau'),
    ('Guatemala', 'Guatemala'),
    ('Guiana', 'Guiana'),
    ('Haiti', 'Haiti'),
    ('Holanda', 'Holanda'),
    ('Honduras', 'Honduras'),
    ('Hungria', 'Hungria'),
    ('Iémen', 'Iémen'),
    ('Ilhas Marshall', 'Ilhas Marshall'),
    ('Ilhas Maurício', 'Ilhas Maurício'),
    ('Ilhas Salomão', 'Ilhas Salomão'),
    ('Índia', 'Índia'),
    ('Indonésia', 'Indonésia'),
    ('Irã', 'Irã'),
    ('Iraque', 'Iraque'),
    ('Irlanda', 'Irlanda'),
    ('Islândia', 'Islândia'),
    ('Israel', 'Israel'),
    ('Itália', 'Itália'),
    ('Jamaica', 'Jamaica'),
    ('Japão', 'Japão'),
    ('Jordânia', 'Jordânia'),
    ('Kiribati', 'Kiribati'),
    ('Kuwait', 'Kuwait'),
    ('Laos', 'Laos'),
    ('Lesoto', 'Lesoto'),
    ('Letônia', 'Letônia'),
    ('Líbano', 'Líbano'),
    ('Libéria', 'Libéria'),
    ('Líbia', 'Líbia'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lituânia', 'Lituânia'),
    ('Luxemburgo', 'Luxemburgo'),
    ('Macedônia do Norte', 'Macedônia do Norte'),
    ('Madagascar', 'Madagascar'),
    ('Malásia', 'Malásia'),
    ('Malawi', 'Malawi'),
    ('Maldivas', 'Maldivas'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marrocos', 'Marrocos'),
    ('Mauritânia', 'Mauritânia'),
    ('Maurícias', 'Maurícias'),
    ('México', 'México'),
    ('Mianmar', 'Mianmar'),
    ('Micronésia', 'Micronésia'),
    ('Moçambique', 'Moçambique'),
    ('Moldávia', 'Moldávia'),
    ('Monaco', 'Mônaco'),
    ('Mongólia', 'Mongólia'),
    ('Montenegro', 'Montenegro'),
    ('Namíbia', 'Namíbia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Nicarágua', 'Nicarágua'),
    ('Níger', 'Níger'),
    ('Nigéria', 'Nigéria'),
    ('Noruega', 'Noruega'),
    ('Nova Zelândia', 'Nova Zelândia'),
    ('Níger', 'Níger'),
    ('Paquistão', 'Paquistão'),
    ('Palau', 'Palau'),
    ('Panamá', 'Panamá'),
    ('Papua Nova Guiné', 'Papua Nova Guiné'),
    ('Paraguai', 'Paraguai'),
    ('Peru', 'Peru'),
    ('Polônia', 'Polônia'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Quênia', 'Quênia'),
    ('República Dominicana', 'República Dominicana'),
    ('República do Congo', 'República do Congo'),
    ('Romênia', 'Romênia'),
    ('Ruanda', 'Ruanda'),
    ('Rússia', 'Rússia'),
    ('São Cristóvão e Névis', 'São Cristóvão e Névis'),
    ('São Marino', 'São Marino'),
    ('São Tomé e Príncipe', 'São Tomé e Príncipe'),
    ('Senegal', 'Senegal'),
    ('Serra Leoa', 'Serra Leoa'),
    ('Seychelles', 'Seychelles'),
    ('Singapura', 'Singapura'),
    ('Somália', 'Somália'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudão', 'Sudão'),
    ('Suriname', 'Suriname'),
    ('Suécia', 'Suécia'),
    ('Suíça', 'Suíça'),
    ('Syria', 'Siria'),
    ('Tadjiquistão', 'Tadjiquistão'),
    ('Tailândia', 'Tailândia'),
    ('Tanzânia', 'Tanzânia'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad e Tobago', 'Trinidad e Tobago'),
    ('Tunísia', 'Tunísia'),
    ('Turcomenistão', 'Turcomenistão'),
    ('Turquia', 'Turquia'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ucrânia', 'Ucrânia'),
    ('Uruguai', 'Uruguai'),
    ('Uzbequistão', 'Uzbequistão'),
    ('Vanuatu', 'Vanuatu'),
    ('Vaticano', 'Vaticano'),
    ('Venezuela', 'Venezuela'),
    ('Vietnã', 'Vietnã'),
    ('Zâmbia', 'Zâmbia'),
    ('Zimbábue', 'Zimbábue')
]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Nome do Filho'       # Placeholder para o campo nome
            }),
            'nascimento': forms.DateInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Data de Nascimento',
                'type': 'date'                      # Especifica o tipo como date para exibir um seletor de datas
            }),
            'nacionalidade': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nacionalidade',
            }, choices=choices_paises),
             'fk_escolaridade': forms.Select(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Selecione a Escolaridade' # Placeholder para orientação
            }),
                'fk_colegio': forms.Select(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Selecione o colégio' # Placeholder para orientação
            }),
           
        }


class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegio
        fields = ['nome', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nome do Colégio'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Endereço do Colégio'
            }),
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nome do Medicamento'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Valor do Medicamento'
            }),
        }
        
class GrauParDoParNoPaisForm(forms.ModelForm):
    class Meta:
        model = GrauParDoParNoPais
        fields = ['grau']
        widgets = {
            'grau': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Grau de Parentesco'
            }),
         
        }        

class LocalAtendimentoForm(forms.ModelForm):
    class Meta:
        model = LocalAtendimento
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Local Atendimento'
            }),
         
        }        
                
class ReligiaoForm(forms.ModelForm):
    class Meta:
        model = Religiao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nome da Religião'
            }),
        }

class ProfissaoForm(forms.ModelForm):
    class Meta:
        model = Profissao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Nome da Profissão'    # Placeholder para orientação
            }),
        }


class TipoDocForm(forms.ModelForm):
    class Meta:
        model = TipoDoc
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Nome do Doc'      # Placeholder para orientação
            }),
        }

class TipoDoacaoForm(forms.ModelForm):
    class Meta:
        model = TipoDoacao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Nome da Doação'      # Placeholder para orientação
            }),
        }

class TipoResidenciaForm(forms.ModelForm):
    class Meta:
        model = TipoResidencia
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Nome da Residência'      # Placeholder para orientação
            }),
        }

class BazarForm(forms.ModelForm):
    class Meta:
        model = Bazar
        fields = ['titulo', 'valorTotal', 'data', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Título do Bazar'     # Placeholder para orientação
            }),
            'valorTotal': forms.NumberInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Valor Total'         # Placeholder para orientação
            }),
            'data': forms.DateInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'type': 'date',
                'placeholder': 'Data'                # Placeholder para orientação
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Descrição do Bazar', # Placeholder para orientação
                'rows': 4                             # Ajusta o número de linhas visíveis
            }),
        }


class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['nome','data', 'custo', 'fk_tipo_doacao']
        labels = {
            'nome':'Nome',
            'data': 'Data',                       # Label para o campo 'data'
            'custo': 'Custo',                     # Label para o campo 'custo'
            # 'fk_refugiado': 'Destinatário',      # Label para o campo 'fk_refugiado'
            'fk_tipo_doacao': 'Tipo de Doação'   # Label para o campo 'fk_tipo_doacao'
        }
        choices_doacao = [
            ('Roupas', 'Roupas'),
            ('Alimentação', 'Alimentação'),
            ('Higiene/Limpeza', 'Higiene/Limpeza'),
            ('Dinheiro', 'Dinheiro'),
            ('Outros', 'Outros'),
        ]
        widgets = {
            'nome': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Selecione o item de doação',
            }, choices=choices_doacao),
            'data': forms.DateInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'type': 'date',
                'placeholder': 'Data da Doação'      # Placeholder para orientação
            }),
            'custo': forms.NumberInput(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Custo da Doação'     # Placeholder para orientação
            }),
            # 'fk_refugiado': forms.Select(attrs={
            #     'class': 'form-control form-input',  # Classe adicional para estilo
            #     'placeholder': 'Selecione o Refugiado' # Placeholder para orientação
            # }),
            'fk_tipo_doacao': forms.Select(attrs={
                'class': 'form-control form-input',  # Classe adicional para estilo
                'placeholder': 'Selecione o Tipo de Doação' # Placeholder para orientação
            }),
        }



class RefugiadoForm(forms.ModelForm):
    class Meta:
        model = Refugiado
        choices_sexo = [
            ('',''),
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
            ('Outro', 'Outro')
        ]
        
        choices_paises = [
    ('',''),
    ('Afeganistão', 'Afeganistão'),
    ('África do Sul', 'África do Sul'),
    ('Albânia', 'Albânia'),
    ('Algéria', 'Algéria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antígua e Barbuda', 'Antígua e Barbuda'),
    ('Arábia Saudita', 'Arábia Saudita'),
    ('Argélia', 'Argélia'),
    ('Argentina', 'Argentina'),
    ('Armênia', 'Armênia'),
    ('Austrália', 'Austrália'),
    ('Áustria', 'Áustria'),
    ('Azerbaijão', 'Azerbaijão'),
    ('Bahamas', 'Bahamas'),
    ('Bahrein', 'Bahrein'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Bielorrússia', 'Bielorrússia'),
    ('Bélgica', 'Bélgica'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermudas', 'Bermudas'),
    ('Bolívia', 'Bolívia'),
    ('Bósnia e Herzegovina', 'Bósnia e Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brasil', 'Brasil'),
    ('Brunei', 'Brunei'),
    ('Bulgária', 'Bulgária'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Camboja', 'Camboja'),
    ('Camarões', 'Camarões'),
    ('Canadá', 'Canadá'),
    ('Cabo Verde', 'Cabo Verde'),
    ('República Centro-Africana', 'República Centro-Africana'),
    ('Chade', 'Chade'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Chipre', 'Chipre'),
    ('Colômbia', 'Colômbia'),
    ('Comores', 'Comores'),
    ('República Democrática do Congo', 'República Democrática do Congo'),
    ('Congo', 'Congo'),
    ('Costa Rica', 'Costa Rica'),
    ('Croácia', 'Croácia'),
    ('Cuba', 'Cuba'),
    ('Chipre', 'Chipre'),
    ('República Tcheca', 'República Tcheca'),
    ('Dinamarca', 'Dinamarca'),
    ('Djibuti', 'Djibuti'),
    ('Dominica', 'Dominica'),
    ('Egito', 'Egito'),
    ('El Salvador', 'El Salvador'),
    ('Emirados Árabes Unidos', 'Emirados Árabes Unidos'),
    ('Equador', 'Equador'),
    ('Eritreia', 'Eritreia'),
    ('Estônia', 'Estônia'),
    ('Eswatini', 'Eswatini'),
    ('Espanha', 'Espanha'),
    ('Estados Unidos', 'Estados Unidos'),
    ('Eslováquia', 'Eslováquia'),
    ('Eslovênia', 'Eslovênia'),
    ('Etiópia', 'Etiópia'),
    ('Fiji', 'Fiji'),
    ('Filipinas', 'Filipinas'),
    ('Finlândia', 'Finlândia'),
    ('França', 'França'),
    ('Gabão', 'Gabão'),
    ('Gâmbia', 'Gâmbia'),
    ('Gana', 'Gana'),
    ('Geórgia', 'Geórgia'),
    ('Granada', 'Granada'),
    ('Guerra', 'Guerra'),
    ('Guiana', 'Guiana'),
    ('Guiné', 'Guiné'),
    ('Guiné-Bissau', 'Guiné-Bissau'),
    ('Guatemala', 'Guatemala'),
    ('Guiana', 'Guiana'),
    ('Haiti', 'Haiti'),
    ('Holanda', 'Holanda'),
    ('Honduras', 'Honduras'),
    ('Hungria', 'Hungria'),
    ('Iémen', 'Iémen'),
    ('Ilhas Marshall', 'Ilhas Marshall'),
    ('Ilhas Maurício', 'Ilhas Maurício'),
    ('Ilhas Salomão', 'Ilhas Salomão'),
    ('Índia', 'Índia'),
    ('Indonésia', 'Indonésia'),
    ('Irã', 'Irã'),
    ('Iraque', 'Iraque'),
    ('Irlanda', 'Irlanda'),
    ('Islândia', 'Islândia'),
    ('Israel', 'Israel'),
    ('Itália', 'Itália'),
    ('Jamaica', 'Jamaica'),
    ('Japão', 'Japão'),
    ('Jordânia', 'Jordânia'),
    ('Kiribati', 'Kiribati'),
    ('Kuwait', 'Kuwait'),
    ('Laos', 'Laos'),
    ('Lesoto', 'Lesoto'),
    ('Letônia', 'Letônia'),
    ('Líbano', 'Líbano'),
    ('Libéria', 'Libéria'),
    ('Líbia', 'Líbia'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lituânia', 'Lituânia'),
    ('Luxemburgo', 'Luxemburgo'),
    ('Macedônia do Norte', 'Macedônia do Norte'),
    ('Madagascar', 'Madagascar'),
    ('Malásia', 'Malásia'),
    ('Malawi', 'Malawi'),
    ('Maldivas', 'Maldivas'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marrocos', 'Marrocos'),
    ('Mauritânia', 'Mauritânia'),
    ('Maurícias', 'Maurícias'),
    ('México', 'México'),
    ('Mianmar', 'Mianmar'),
    ('Micronésia', 'Micronésia'),
    ('Moçambique', 'Moçambique'),
    ('Moldávia', 'Moldávia'),
    ('Monaco', 'Mônaco'),
    ('Mongólia', 'Mongólia'),
    ('Montenegro', 'Montenegro'),
    ('Namíbia', 'Namíbia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Nicarágua', 'Nicarágua'),
    ('Níger', 'Níger'),
    ('Nigéria', 'Nigéria'),
    ('Noruega', 'Noruega'),
    ('Nova Zelândia', 'Nova Zelândia'),
    ('Níger', 'Níger'),
    ('Paquistão', 'Paquistão'),
    ('Palau', 'Palau'),
    ('Panamá', 'Panamá'),
    ('Papua Nova Guiné', 'Papua Nova Guiné'),
    ('Paraguai', 'Paraguai'),
    ('Peru', 'Peru'),
    ('Polônia', 'Polônia'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Quênia', 'Quênia'),
    ('República Dominicana', 'República Dominicana'),
    ('República do Congo', 'República do Congo'),
    ('Romênia', 'Romênia'),
    ('Ruanda', 'Ruanda'),
    ('Rússia', 'Rússia'),
    ('São Cristóvão e Névis', 'São Cristóvão e Névis'),
    ('São Marino', 'São Marino'),
    ('São Tomé e Príncipe', 'São Tomé e Príncipe'),
    ('Senegal', 'Senegal'),
    ('Serra Leoa', 'Serra Leoa'),
    ('Seychelles', 'Seychelles'),
    ('Singapura', 'Singapura'),
    ('Somália', 'Somália'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudão', 'Sudão'),
    ('Suriname', 'Suriname'),
    ('Suécia', 'Suécia'),
    ('Suíça', 'Suíça'),
    ('Syria', 'Siria'),
    ('Tadjiquistão', 'Tadjiquistão'),
    ('Tailândia', 'Tailândia'),
    ('Tanzânia', 'Tanzânia'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad e Tobago', 'Trinidad e Tobago'),
    ('Tunísia', 'Tunísia'),
    ('Turcomenistão', 'Turcomenistão'),
    ('Turquia', 'Turquia'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ucrânia', 'Ucrânia'),
    ('Uruguai', 'Uruguai'),
    ('Uzbequistão', 'Uzbequistão'),
    ('Vanuatu', 'Vanuatu'),
    ('Vaticano', 'Vaticano'),
    ('Venezuela', 'Venezuela'),
    ('Vietnã', 'Vietnã'),
    ('Zâmbia', 'Zâmbia'),
    ('Zimbábue', 'Zimbábue')
]


        fields = [
            'nome', 'nascimento', 'tipo_doc', 'nacionalidade', 'sexo',
            'endereco', 'telefone', 'email', 'necessidade_especial',
            'renda_mensal', 'data_chegada', 'descricao_chegada',
            'quantidade_familiares', 'hipertenso', 'diabetico',
            'relatorio_social', 'trabalha', 'local_trabalho', 'numero_doc',
            'deficiencia', 'parente_no_pais','tipo_residencia','profissao','fk_escolaridade','tipo_deficiencia'

        ]

        labels = {
            'tipo_doc':'Tipo de Documento',
            'fk_escolaridade':'Escolaridade',
            'tipo_deficiencia':'Tipo de deficiência'
        }

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Nome do Refugiado'
            }),
            
            'nascimento': forms.DateInput(attrs={
                'class': 'form-control form-input',
                'type': 'date',
                'placeholder': 'Data de Nascimento'
            }),
            'tipo_doc': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Tipo de Documento',
                'id':'tipo_doc'
            }),
              'profissao': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Profissao',
                'id':'profissao'
            }),
            'fk_escolaridade': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Escolaridade',
                'id':'escolaridade'
            }),
            
            'tipo_residencia': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Tipo de Residência',
                'id':'tipo_residencia'
            }),
  'nacionalidade': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Selecione o Sexo',
            }, choices=choices_paises),
            'sexo': forms.Select(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Selecione o Sexo',
            }, choices=choices_sexo),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Endereço'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'id':'telefone',
                'placeholder': 'Telefone',
                'placeholder': '(XX) XXXXX-XXXX'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Email'
            }),
            'necessidade_especial': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'renda_mensal': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Renda Mensal'
            }),
            'data_chegada': forms.DateInput(attrs={
                'class': 'form-control form-input',
                'type': 'date',
                'placeholder': 'Data de Chegada'
            }),
            'descricao_chegada': forms.Textarea(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Descrição da Chegada',
                'rows': 4
            }),
            'quantidade_familiares': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Quantidade de Familiares'
            }),
            #  'filhos': forms.CheckboxInput(attrs={
            #     'class': 'form-check-input',
            #     'id':'id_filhos'
            # }),
            # 'quantidade_filhos': forms.NumberInput(attrs={
            #     'class': 'form-control form-input',
            #     'placeholder': 'Quantidade de Filhos',
            #     'id':'quantidade_filhos',
            # }),
            'hipertenso': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'diabetico': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'relatorio_social': forms.Textarea(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Relatório Social',
                'rows': 4
            }),
            'trabalha': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id':'id_trabalha'
            }),
            'local_trabalho': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Local de Trabalho'
            }),
             'tipo_deficiencia': forms.TextInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Tipo de deficiência',
                'id':'id_tipo_deficiencia'
            }),
            'numero_doc': forms.NumberInput(attrs={
                'class': 'form-control form-input',
                'placeholder': 'Número do Documento',
            }),
            
            'deficiencia': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id':'id_deficiencia'
            }),
            'parente_no_pais': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            
        }

        
