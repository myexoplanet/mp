from django import forms
from .models import Contacto
from django.forms import ModelForm, DateInput, DateField
import datetime

class ContactForm(forms.ModelForm):
	
	class Meta:
		model = Contacto
		fields = [
			'run',
			'nombre',
			'apellido',
			'correo',
			'fecha_nacimiento',
			'telefono',
			'region',
			'comuna',
			'tipovivienda',
			'mensaje',
			]

		labels = {
			'run':'Rut',
			'nombre':'Nombre',
			'apellido':'Apellido',
			'correo':'Correo',
			'fecha_nacimiento':'Fecha de nacimiento',
			'telefono': 'Telefono',
			'region': 'Region',
			'comuna': 'Comuna',
			'tipovivienda':'Tipo de vivienda',
			'mensaje':'Mensaje',
			}
		widgets = {
			'run': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(),
			'apellido': forms.TextInput(),
			'fecha_nacimiento': forms.SelectDateWidget(years=range(datetime.datetime.now().year - 100, datetime.datetime.now().year)),
			'telefono': forms.TextInput(),
			'region': forms.TextInput(),
			'comuna': forms.TextInput(),
			'tipovivienda': forms.Select(),
			'mensaje': forms.Textarea(),        
			}
