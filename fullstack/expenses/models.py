from django.db import models
from django.contrib.auth.models import User
from categories.models import ExpenseCategory
from django.utils import timezone
import pytz


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(ExpenseCategory)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Expense ID: {self.expense_id}, User: {self.user.username}, Categories: {[category.name for category in self.categories.all()]}"

    def save(self, *args, **kwargs):
        if not self.date.tzinfo:
            tz = pytz.timezone('Europe/Moscow')
            self.date = tz.localize(self.date)
        super().save(*args, **kwargs)