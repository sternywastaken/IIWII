from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import models


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateRecordForm(models.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class PostComment(models.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
