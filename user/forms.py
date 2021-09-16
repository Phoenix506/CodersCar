from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class LoginForm(forms.Form):
    username = forms.CharField(label='İstifadəçi adi')
    password = forms.CharField(label='Şifrə', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = PhoneNumberField(region="AZ", widget=forms.TextInput(attrs={"placeholder": "Nömrənizi qeyd edin"}),
                                label=("Telefon Nömrəniz"))
    password = forms.CharField(max_length=20, label="Şifrə", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu nömrə artıq qeydiyyatdan keçib")
        return username


class UserUpdateForm(forms.ModelForm):
    username = PhoneNumberField(region="AZ", widget=forms.TextInput(attrs={"placeholder": "Nömrənizi qeyd edin"}),
                                label=("Telefon Nömrəniz"))
    first_name = forms.CharField(label=("Adınız"))
    last_name = forms.CharField(label=("Soyadınız"))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
