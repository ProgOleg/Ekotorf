# Generated by Django 2.2.16 on 2021-03-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20210304_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='note',
            field=models.CharField(default=None, max_length=5000, null=True, verbose_name='Заметка'),
        ),
    ]
