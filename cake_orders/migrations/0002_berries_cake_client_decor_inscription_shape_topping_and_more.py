# Generated by Django 4.1.3 on 2022-11-24 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='berries')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='name')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('berries', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cake_orders.berries', verbose_name='Berries for the cake')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_account', models.CharField(max_length=200, verbose_name='telegram account for communication')),
                ('pd_read', models.BooleanField(default=False, verbose_name='personal data agreement read?')),
            ],
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='decor')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='inscription')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='shape')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='topping')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=400, verbose_name='comment for order and delivery')),
                ('client_delivery_datetime', models.DateTimeField(verbose_name="client's date and time of the delivery")),
                ('forecast_delivery_datetime', models.DateTimeField(verbose_name="client's date and time of the delivery")),
                ('delivery_address', models.CharField(max_length=200, verbose_name='delivery address')),
                ('is_urgent', models.BooleanField(default=False, verbose_name='is order urgent?')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('cake', models.ManyToManyField(to='cake_orders.cake', verbose_name='cakes in the order')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_orders.client', verbose_name='client')),
            ],
        ),
        migrations.AddField(
            model_name='cake',
            name='decor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cake_orders.decor', verbose_name='Decor for the cake'),
        ),
        migrations.AddField(
            model_name='cake',
            name='inscription',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cake_orders.inscription', verbose_name='Inscription for the cake'),
        ),
        migrations.AddField(
            model_name='cake',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_orders.level', verbose_name='levels in cake'),
        ),
        migrations.AddField(
            model_name='cake',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_orders.shape', verbose_name='Shape of the cake'),
        ),
        migrations.AddField(
            model_name='cake',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_orders.topping', verbose_name='Topping for the cake'),
        ),
    ]
