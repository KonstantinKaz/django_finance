from django.db import models
from django.contrib.auth.models import User
from categories.models import ExpenseCategory

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Expense ID: {self.expense_id}, User: {self.user.username}, Category: {self.category.name}"
