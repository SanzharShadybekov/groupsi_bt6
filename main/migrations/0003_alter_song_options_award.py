# Generated by Django 5.0.3 on 2024-03-18 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_musician_options_song'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'Музыка', 'verbose_name_plural': 'Песни'},
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('song', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.song')),
            ],
        ),
    ]
