from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class SignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Password Confirmation")
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    field_order = ['full_name', 'email', 'password', 'password_2']

    class Meta:
        model = CustomUser
        exclude = ['is_admin', 'is_active', 'last_login']

    def clean(self):
        cleaned_data = super().clean()
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password_2']
        if pass1 != pass2:
            raise ValueError("Password does not match!")
        return cleaned_data

    def save(self, commit=True):
        pass1 = self.cleaned_data['password']
        user = super().save(commit=False)
        user.set_password(pass1)
        user.save()
        return user
