# Sistema de Gestão para Centro de Atendimento a Refugiados

Sistema web desenvolvido em Python com Django para apoiar a gestão de atendimentos, cadastros, acompanhamento social e organização operacional de um centro de atendimento a refugiados.

O projeto foi pensado para centralizar informações de refugiados, familiares, documentos, necessidades específicas, registros de atendimentos, doações e bazar, além de disponibilizar indicadores e relatórios por meio de um painel administrativo.

## Visão geral

Este sistema permite:

- cadastrar refugiados e seus dependentes;
- registrar dados pessoais, residência, escolaridade, profissão e condição de saúde;
- acompanhar locais de atendimento e atendentes responsáveis;
- gerenciar arquivos/documentos digitais vinculados ao refugiado;
- registrar doações e itens de bazar;
- consultar indicadores por nacionalidade, sexo, medicamentos, trabalho e atendimentos;
- manter listas de referência do sistema, como tipos de documento, tipos de residência, profissões, escolas e medicamentos.

## Funcionalidades principais

### 1. Cadastro e gestão de refugiados
- Dados pessoais e de contato;
- data de chegada, renda mensal e descrição do acolhimento;
- informações sobre famílias, filhos e parentes no país;
- registros de deficiência, medicamentos e necessidades especiais;
- vínculo com locais de atendimento e grau de parentesco.

### 2. Acompanhamento de atendimento
- associação de refugiados a atendentes;
- registro de locais de atendimento;
- estrutura para acompanhamento social e cuidado individual.

### 3. Gestão de documentação
- upload de documentos digitais;
- vinculação direta ao refugiado;
- possibilidade de exclusão de arquivos do cadastro.

### 4. Doações e bazar
- cadastro de tipos de doação;
- registro de doações com custo e data;
- gestão de bazar com título, valor total, descrição e data.

### 5. Painel e indicadores
- dashboard com informações consolidadas;
- gráficos por sexo, nacionalidade, medicamentos e trabalho;
- métricas por atendente e dados de parceria/comunidade.

### 6. Configurações administrativas
- configuração de categorias e listas de apoio do sistema;
- manutenção de tipos de documento, profissões, escolaridade, residências, locais de atendimento e medicamentos.

## Tecnologias

- Python 3
- Django 5.1.3
- SQLite (configuração padrão)
- HTML, CSS e JavaScript
- Bootstrap/templating do Django

## Estrutura do projeto

```text
.
├── manage.py
├── requirements.txt
├── README.md
├── refugiados/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── refugiados_app/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── templates/
├── static/
│   ├── css/
│   └── img/
└── db.sqlite3
```

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.10 ou superior
- pip
- virtualenv (opcional, mas recomendado)
- Git
- editor de código como VS Code, PyCharm ou similar

## Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositório>
cd gestao-centro-atendimento-refugiados
```

2. Crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:

```bash
python manage.py makemigrations refugiados_app
python manage.py migrate
```

5. Coletar arquivos estáticos:

```bash
python manage.py collectstatic
```

6. Crie um usuário administrador:

```bash
python manage.py createsuperuser
```

7. Inicie o servidor:

```bash
python manage.py runserver
```

8. Acesse a aplicação no navegador:

```text
http://127.0.0.1:8000
```

## Acesso ao sistema

- Página inicial do sistema: dashboard principal
- Login: `/login/`
- Cadastro de usuários e atendentes: `/register/`
- Dashboard: `/`
- Cadastro de refugiados: `/refugiado/`
- Doações: `/doacao/`
- Bazar: `/bazar/`
- Configurações: `/config/`

## Usuários e perfis

O sistema permite cadastro de usuários e atendentes com perfis de:

- Atendente
- Gerente

Esses perfis são utilizados para diferenciar acesso e responsabilidades dentro do ambiente administrativo.

## Configuração do banco de dados

O projeto está configurado para usar SQLite por padrão, o que facilita a execução local e testes iniciais.

Se necessário, a configuração pode ser adaptada para PostgreSQL em `refugiados/settings.py`.

## Boas práticas

- manter o ambiente virtual ativo durante o desenvolvimento;
- sempre rodar `python manage.py migrate` após alterações nos modelos;
- usar `python manage.py createsuperuser` para acessar o painel administrativo;
- evitar expor a `SECRET_KEY` e informações sensíveis em ambientes reais.

## Observações

Este projeto foi desenvolvido como sistema acadêmico/profissional para apoiar a gestão de acolhimento e atendimento a refugiados. Em produção, é recomendado:

- revisar segurança e autenticação;
- ajustar configurações de ambiente;
- configurar banco de dados robusto;
- reforçar backup e controle de acesso;
- validar fluxos de negócio com usuários finais.

## Licença

Este projeto está disponível para uso acadêmico e institucional. Verifique com a equipe responsável antes de reutilizar em produção ou em ambientes externos.

## Contato

Para dúvidas, melhorias ou apoio na implantação, consulte o responsável pelo projeto ou a equipe desenvolvedora.
