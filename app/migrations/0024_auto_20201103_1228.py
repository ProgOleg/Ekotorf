# Generated by Django 2.2.16 on 2020-11-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20201103_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='working_time',
            field=models.CharField(max_length=50, verbose_name='Время работы'),
        ),
    ]
