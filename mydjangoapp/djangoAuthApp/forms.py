from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo_electronico']
    
    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        if not forms.EmailField().clean(correo_electronico):
            raise forms.ValidationError("Por favor ingrese un correo electrónico válido.")
        return correo_electronico