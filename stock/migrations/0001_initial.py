# Generated by Django 5.0.7 on 2024-09-11 09:40

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catogery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.FileField(blank=True, null=True, upload_to='Product-Catogery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('phone_number', models.PositiveBigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('table_number', models.IntegerField(primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=100, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9.\\-\\s]+$', code='Invalide name', message='Invalid data format. Only letters, numbers, and hyphens are allowed.')])),
                ('photo', models.FileField(blank=True, null=True, upload_to='product_image')),
                ('product_code', models.PositiveIntegerField(blank=True, default=0, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user_price', models.PositiveBigIntegerField()),
                ('catogery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='stock.catogery')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stock.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('home_price', models.PositiveBigIntegerField()),
                ('remaining_quantity', models.PositiveBigIntegerField(blank=True, null=True)),
                ('remaining_quantity_total_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('added_quantity', models.PositiveBigIntegerField(blank=True, null=True)),
                ('added_quantity_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('initial_quantity', models.PositiveBigIntegerField()),
                ('initial_quantity_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock_product', to='stock.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
