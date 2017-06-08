from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }