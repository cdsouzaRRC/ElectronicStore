# Generated by Django 4.0.5 on 2022-07-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0024_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
