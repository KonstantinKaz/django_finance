from django import forms
from .models import Expense
from categories.models import ExpenseCategory

class ExpenseForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=ExpenseCategory.objects.all())

    class Meta:
        model = Expense
        fields = ['expense_name', 'categories', 'date', 'amount', 'description']
        widgets = {
            'user': forms.HiddenInput(),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'categories': forms.SelectMultiple(attrs={'class': 'select2'}),
        }
