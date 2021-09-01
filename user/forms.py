from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='İstifadəçi adi')
    password = forms.CharField(label='Şifrə', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="İstifadəçi adı")
    password = forms.CharField(max_length=20, label="Şifrə", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        name = self.cleaned_data.get('name')
        surname = self.cleaned_data.get('surname')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError('Şifrələr eyni deyil')

        else:
            values = {'username': username, 'password': password}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
