# Generated by Django 4.2.13 on 2024-05-25 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['currency']},
        ),
    ]