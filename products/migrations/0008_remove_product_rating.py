# Generated by Django 3.2 on 2022-01-11 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rating_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]