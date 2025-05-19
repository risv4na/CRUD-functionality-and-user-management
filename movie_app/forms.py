from django.forms import ModelForm
from django import forms
from .models import Movies,CensorDetail

class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        exclude = ['censor_details']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class CensorInfoForm(ModelForm):
    class Meta:
        model = CensorDetail
        fields = ["rating", "certified_by" ]


