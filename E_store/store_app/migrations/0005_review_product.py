# Generated by Django 4.0.5 on 2022-06-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.CharField(max_length=200, null=True),
        ),
    ]