# Generated by Django 4.1.7 on 2023-06-18 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.city', verbose_name='Cuidad'),
        ),
    ]
