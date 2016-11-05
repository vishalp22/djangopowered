from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    fullname = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullname', 'email']
