# Generated by Django 4.0.5 on 2022-07-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0023_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]