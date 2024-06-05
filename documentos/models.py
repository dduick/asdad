from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Create your models here.
select_documentos = [
    ('Cédula de Identidad','Cédula de Identidad'),
    ('Licencia de Conducir','Licencia de Conducir'),
    ('Padrón','Padrón'),
    ('Permiso de Circulación','Permiso de Circulación'),
    ('Revisión Técnica','Revisión Técnica'),
    ('SOAP','SOAP')
    ] 


class Documentos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_doc = models.AutoField(primary_key=True)
    tipo_doc = models.CharField(max_length=50, choices=select_documentos)
    link_doc = models.CharField(max_length=250)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.user, self.id_doc, self.tipo_doc, self.link_doc)
    
