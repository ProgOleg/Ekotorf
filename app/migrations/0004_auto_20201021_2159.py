# Generated by Django 2.2.16 on 2020-10-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_faq_firstwindow_privacypolicy_product_secondwindow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='picture',
            field=models.ImageField(upload_to='Feedback/', verbose_name='Фото'),
        ),
    ]
