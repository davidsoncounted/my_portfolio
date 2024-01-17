from .models import Rate, Portfolio
from django import forms
from django.forms import ModelForm


class ref_form(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['name', 'review', 'image', 'occupation']
        widgets ={
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'review': forms.Textarea(attrs={'placeholder': 'Write your reviews or reference here'}),
            'occupation': forms.TextInput(attrs={  'placeholder': 'Enter your job'}),
            'image': forms.ClearableFileInput(attrs={ 'placeholder': 'Pls paste your picture'}),
            'image': forms.ClearableFileInput(attrs={'class': 'image-field'}),
        }

class post_form(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'




