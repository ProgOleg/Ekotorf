# Generated by Django 2.2.16 on 2020-11-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20201103_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegram',
            options={'verbose_name_plural': 'Telegram'},
        ),
        migrations.AlterModelOptions(
            name='viber',
            options={'verbose_name_plural': 'Viber'},
        ),
        migrations.AlterModelOptions(
            name='whatsapp',
            options={'verbose_name_plural': 'Whatsapp'},
        ),
        migrations.AlterField(
            model_name='person',
            name='tell',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='telephonenumbers',
            name='tell',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
    ]
