# Generated by Django 4.2.2 on 2023-06-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('incomes', '0002_alter_income_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='category',
        ),
        migrations.AddField(
            model_name='income',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.incomecategory'),
        ),
    ]