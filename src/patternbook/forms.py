from django import  forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name', 'company', 'phone', 'note', 'newsletter']
