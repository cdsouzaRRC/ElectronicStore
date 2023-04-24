# Generated by Django 4.1 on 2022-08-13 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_app', '0034_alter_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_date',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Packed', 'PACKED'), ('Shipping', 'SHIPPING'), ('Delivered', 'DELIVERED')], default='Pending', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('town_city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postcode', models.IntegerField()),
                ('phone', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]