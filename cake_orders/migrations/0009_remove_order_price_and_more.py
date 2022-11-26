# Generated by Django 4.1.3 on 2022-11-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_orders', '0008_alter_client_tg_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='forecast_delivery_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='forecast date and time of the delivery'),
        ),
    ]