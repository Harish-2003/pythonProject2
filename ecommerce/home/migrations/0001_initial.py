# Generated by Django 4.2.3 on 2023-07-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('orign', models.CharField(max_length=200)),
            ],
        ),
    ]
