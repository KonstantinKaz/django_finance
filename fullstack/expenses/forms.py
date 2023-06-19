from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name', 'category', 'date', 'amount', 'description']
        widgets = {
            'user': forms.HiddenInput(),
        }
