from django.db import models
from django.contrib.auth.models import User
from categories.models import IncomeCategory

class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Income ID: {self.income_id}, User: {self.user.username}, Category: {self.category.name}"
