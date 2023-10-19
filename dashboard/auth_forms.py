from django import forms


class LoginForm(forms.Form):
    inputUsername = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput)
    inputPassword = forms.CharField(label="Your password", max_length=100, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    inputUserName = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput)
    inputEmail = forms.EmailField(label="Your email", max_length=100, widget=forms.EmailInput)
    inputPassword = forms.CharField(label="Your password", max_length=100, widget=forms.PasswordInput)
    inputPasswordConfirm = forms.CharField(label="Your password", max_length=100, widget=forms.PasswordInput)
