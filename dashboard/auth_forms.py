from django import forms


class LoginForm(forms.Form):
    inputUsername = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput)
    inputPassword = forms.CharField(label="Your password", max_length=100, widget=forms.PasswordInput)
