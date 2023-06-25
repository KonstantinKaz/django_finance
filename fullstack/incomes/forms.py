from django import forms
from .models import Income
from categories.models import IncomeCategory

class IncomeForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=IncomeCategory.objects.all())

    class Meta:
        model = Income
        fields = ['income_name', 'categories', 'date', 'amount', 'description']
        widgets = {
            'user': forms.HiddenInput(),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'categories': forms.SelectMultiple(attrs={'class': 'select2'}),
        }