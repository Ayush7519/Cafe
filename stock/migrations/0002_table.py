# Generated by Django 5.0.7 on 2024-08-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
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
    ]
