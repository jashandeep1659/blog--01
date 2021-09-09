
from django.forms import ModelForm
from django import forms
from blogs.models import *

class NewCommnetForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email','comment','full_name','blog',]
