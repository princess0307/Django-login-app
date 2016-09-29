from django import forms
from django.forms import ModelForm
from .models import Reg


class RegForm(ModelForm):

    class Meta:
        model = Reg
        fields=['name','email','password']
