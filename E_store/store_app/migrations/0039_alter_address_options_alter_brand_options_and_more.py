# Generated by Django 4.1 on 2022-08-14 04:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0038_alter_address_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Brand'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': 'Color'},
        ),
        migrations.AlterModelOptions(
            name='contact_us',
            options={'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': 'Faq'},
        ),
        migrations.AlterModelOptions(
            name='filter_price',
            options={'verbose_name_plural': 'Filter_Price'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'Order Items'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Review'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Slider'},
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('\\d{6}')]),
        ),
    ]