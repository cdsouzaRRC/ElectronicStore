# Generated by Django 4.1 on 2022-08-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0035_remove_product_created_date_orderitem_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
