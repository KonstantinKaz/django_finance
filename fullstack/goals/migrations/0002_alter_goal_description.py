# Generated by Django 4.2.2 on 2023-06-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
