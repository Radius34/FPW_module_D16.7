# Generated by Django 4.2.5 on 2023-10-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('confirmation_code', models.CharField(max_length=20)),
                ('is_confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
