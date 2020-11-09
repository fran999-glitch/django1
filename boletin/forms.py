from django import forms

from .models import Registrado


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")
        if not extension == "cl": 
         raise forms.ValidationError("por favor utiliza un email con la extension .cl")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre



class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)