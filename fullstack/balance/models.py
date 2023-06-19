from django.db import models
from django.contrib.auth.models import User

class Balance(models.Model):
    balance_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"Balance ID: {self.balance_id}, User: {self.user.username}"
