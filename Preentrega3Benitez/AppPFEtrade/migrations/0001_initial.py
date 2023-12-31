# Generated by Django 4.2.5 on 2023-09-20 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('ticker', models.CharField(max_length=5)),
                ('quantity', models.FloatField(max_length=2)),
                ('precio', models.FloatField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('ticker', models.CharField(max_length=5)),
                ('quantity', models.FloatField(max_length=10000)),
                ('price', models.FloatField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('ticker', models.CharField(max_length=5)),
                ('quantity', models.FloatField()),
                ('precio', models.FloatField()),
            ],
        ),
    ]
