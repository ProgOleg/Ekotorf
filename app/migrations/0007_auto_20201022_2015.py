# Generated by Django 2.2.16 on 2020-10-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_applications_person_productgalleryphoto_productgalleryvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.CharField(max_length=1000, verbose_name='Описание'),
        ),
    ]
