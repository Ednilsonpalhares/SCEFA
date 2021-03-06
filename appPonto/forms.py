from django.forms import ModelForm, forms, DateInput
from appPonto.models import *
from django import forms

class FuncionarioForm(ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)
    class Meta:
        model = Funcionario
        fields = (
        'nome', 'matricula', 'cpf', 'dataNascimento', 'telefone', 'cargo', 'Email', 'sexo', 'salario',
        'foto', 'situacao', 'senha')

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields  = ('descricao',)

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields  = ('nome_funcao','departamento')

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ('cargahoraria', 'dias', 'pessoa')

class DiasSemExpedienteForm(ModelForm):
    class Meta:
        model = DiasSemExpediente
        fields  = ('descricao','data')