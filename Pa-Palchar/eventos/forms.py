from django import forms
from django.forms import ModelForm
from .models import Venue


#create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','phone','email_address')
        #create styles
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del lugar'}),
                  'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
                  'phone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numero de contacto'}),
                  'email_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electronico'})
                  }
