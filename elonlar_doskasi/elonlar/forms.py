from django import forms
from .models import Elon

class ElonForm(forms.ModelForm):
    class Meta:
        mode = Elon
        fields = ['title', 'description', 'price']