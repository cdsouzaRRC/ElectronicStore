# Generated by Django 4.0.5 on 2022-07-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0026_delete_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_rating',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
