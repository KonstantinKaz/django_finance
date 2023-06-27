from django.db import models
from django.contrib.auth.models import User
from balance.models import Balance


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_remaining_amount(self):
        balance = Balance.objects.get(user=self.user)
        remaining_amount = self.amount - balance.total_balance
        return remaining_amount
