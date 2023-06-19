from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_name', 'category', 'date', 'amount', 'description']
        widgets = {
            'user': forms.HiddenInput(),
        }
