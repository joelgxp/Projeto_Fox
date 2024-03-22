from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)    
    ativo = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return f"{self.username, self.email, self.password, self.last_login, self.is_superuser, self.is_staff, self.is_active, self.date_joined, self.ativo}"
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    renavam = models.CharField(max_length=11)
    chassi = models.CharField(max_length=45, null=True, blank=True)
    cor = models.CharField(max_length=25)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    ano_fabricacao = models.CharField(max_length=4)
    ano_fabricacao_modelo = models.CharField(max_length=4)
    data_entrada = models.DateField()
    complemento = models.CharField(max_length=250, null=True, blank=True)
    status = models.BooleanField(default=0)
    vendido = models.BooleanField(default=0)
    
    def __str__(self):
        return f"{self.id, self.placa, self.renavam, self.chassi, self.cor, self.marca, self.modelo, self.ano_fabricacao, self.ano_fabricacao_modelo, self.data_entrada, self.complemento, self.status, self.vendido}"
    
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={'type': 'text', 'minlength': '7', 'size': '8'}),
            'marca': forms.DateInput(attrs={'type': 'text', 'size': '10'}),
            'modelo': forms.DateInput(attrs={'type': 'text', 'size': '10'}),
            'data_entrada': forms.DateInput(attrs={'type': 'date', 'size': '10'}),
            'ano_fabricacao': forms.DateInput(attrs={'type': 'number', 'min': '1900', 'max': '2100'}),
            'ano_fabricacao_modelo': forms.DateInput(attrs={'type': 'number', 'min': '1900', 'max': '2100'}),
            'cor' : forms.TextInput(attrs={'type': 'text', 'size': '15'}),
            'complemento': forms.Textarea(attrs={'rows': 3}),
        }
        
class Servico(models.Model):
    nome = models.CharField(max_length=45, null=False, blank=False)
    tempo_execucao = models.CharField(max_length=10, null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    ordem_servico = models.ForeignKey('OrdemServico', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
class OrdemServico(models.Model):
    data = models.DateField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return f"OS: {self.data, self.veiculo, self.status}"
    
class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['data']
    
