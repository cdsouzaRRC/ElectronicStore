# Generated by Django 4.1 on 2022-08-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0036_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=12345, max_length=50),
            preserve_default=False,
        ),
    ]
