# Generated by Django 4.0.5 on 2022-07-10 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0027_product_average_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='average_rating',
        ),
    ]
