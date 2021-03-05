# Generated by Django 2.2.16 on 2021-03-05 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20210304_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='geography',
            field=models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='География'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='note',
            field=models.CharField(blank=True, default=None, max_length=5000, null=True, verbose_name='Заметка'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Person', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='geomarker',
            name='latitude',
            field=models.CharField(max_length=100, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='geomarker',
            name='longitude',
            field=models.CharField(max_length=100, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
