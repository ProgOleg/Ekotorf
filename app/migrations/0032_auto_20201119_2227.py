# Generated by Django 2.2.16 on 2020-11-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20201119_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='date_ready',
            field=models.DateTimeField(default=None, null=True, verbose_name='Датф готовности'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('processing', 'В обработке'), ('success', 'Успех'), ('refusing', 'Отказ')], default='new', max_length=30, verbose_name='Статус заявки'),
        ),
    ]
