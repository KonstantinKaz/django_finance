# Generated by Django 4.2.2 on 2023-06-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('expenses', '0003_alter_expense_expense_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.AddField(
            model_name='expense',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.expensecategory'),
        ),
    ]
