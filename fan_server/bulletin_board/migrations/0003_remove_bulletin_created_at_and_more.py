# Generated by Django 4.2.5 on 2023-10-03 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0002_bulletin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletin',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bulletin',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('bulletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.bulletin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.user')),
            ],
        ),
    ]
