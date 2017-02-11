from django import forms


from .models import UserMessage

class LoginForm(forms.Form):
    username = forms.CharField(required=True) #required=True 为必填
    password = forms.CharField(required=True, min_length=5)
