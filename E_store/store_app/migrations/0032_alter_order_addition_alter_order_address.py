# Generated by Django 4.0.5 on 2022-07-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0031_rename_cartorder_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='addition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
