from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class Atendente(models.Model):
    # Definir os grupos possíveis
    GRUPOS = [
        ('Atendente', 'Atendente'),
        ('Gerente', 'Gerente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='atendente')
    nome = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)
    rg = models.IntegerField(null=False)
    cpf = models.IntegerField(null=False)
    nascimento = models.DateField(null=False)
    endereco = models.CharField(max_length=255)
    grupo = models.CharField(max_length=20, choices=GRUPOS)

    def __str__(self):
        return f"{self.nome} ({self.get_grupo_display()})"

class TipoDoacao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class TipoDoc(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class TipoResidencia(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
    
class Profissao(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
    

class Escolaridade(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
    


class Medicamento(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    

class GrauParDoParNoPais(models.Model):
    grau = models.CharField(max_length=255)
    
    

class LocalAtendimento(models.Model):
    nome = models.CharField(max_length=255)
                
class Refugiado(models.Model):
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    tipo_doc = models.ForeignKey(TipoDoc,blank=True, null=True, on_delete=models.CASCADE)
    tipo_residencia = models.ForeignKey(TipoResidencia, on_delete=models.CASCADE)
    profissao = models.ForeignKey(Profissao, on_delete=models.CASCADE,null=True, blank=True)
    fk_escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE,null=True)
    nacionalidade = models.CharField(max_length=255,null=False,blank=False)
    sexo = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    necessidade_especial = models.BooleanField()
    renda_mensal = models.FloatField()
    data_chegada = models.DateField()
    descricao_chegada = models.TextField()
    quantidade_familiares = models.IntegerField()
    hipertenso = models.BooleanField()
    diabetico = models.BooleanField()
    relatorio_social = models.TextField()
    trabalha = models.BooleanField()
    local_trabalho = models.CharField(max_length=255,blank=True)
    numero_doc = models.IntegerField( null=True, blank=True)
    deficiencia = models.BooleanField()
    tipo_deficiencia = models.CharField(max_length=255,null=True, blank=True)
    parente_no_pais = models.BooleanField()
    medicamentos = models.ManyToManyField(Medicamento, through='Utiliza')
    GrauParDoParNoPais = models.ManyToManyField(GrauParDoParNoPais, through='Tem')
    LocalAtendimento = models.ManyToManyField(LocalAtendimento, through='Atendido')

    def __str__(self):
        return self.nome



    
class Religiao(models.Model):
    nome = models.CharField(max_length=255)


class Colegio(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome}"



class Filho(models.Model):
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=255)
    fk_refugiado = models.ForeignKey(Refugiado, on_delete=models.CASCADE)
    fk_colegio = models.ForeignKey(Colegio, null=True, blank=True,on_delete=models.CASCADE)
    fk_escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE,null=True,blank=True)








class DocumentosArquivoDigital(models.Model):
    arquivo = models.FileField(upload_to='documentos/')
    fk_refugiado = models.ForeignKey(Refugiado, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.fk_refugiado} tem {self.arquivo}"
    

class Doacao(models.Model):
    nome = models.CharField(max_length=35)
    data = models.DateField()
    custo = models.FloatField()
    # fk_refugiado = models.ForeignKey(Refugiado, on_delete=models.CASCADE)
    fk_tipo_doacao = models.ForeignKey(TipoDoacao, on_delete=models.CASCADE,null=False)



class Utiliza(models.Model):
    fk_refugiado = models.ForeignKey(Refugiado, on_delete=models.SET_NULL, null=True)
    fk_medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.fk_refugiado} usa {self.fk_medicamento}"

class Atendido(models.Model):
    fk_refugiado = models.ForeignKey(Refugiado, on_delete=models.SET_NULL, null=True)
    fk_local_atendimento = models.ForeignKey(LocalAtendimento, on_delete=models.SET_NULL, null=True)  # Ajustado
    fk_atendente = models.ForeignKey(Atendente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.fk_refugiado} - {self.fk_atendente}"


class Tem(models.Model):
    fk_refugiado = models.ForeignKey(Refugiado, on_delete=models.SET_NULL, null=True)
    fk_grauParDoParNoPais = models.ForeignKey(GrauParDoParNoPais, on_delete=models.SET_NULL, null=True)


class Bazar(models.Model):
    titulo = models.CharField(max_length=55)
    valorTotal = models.FloatField()
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

