# Generated by Django 2.2.16 on 2020-10-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201021_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('entry', models.TextField(verbose_name='Запись')),
            ],
        ),
        migrations.CreateModel(
            name='FirstWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=150)),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField(verbose_name='Запись')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('specification', models.CharField(max_length=500, verbose_name='Описание')),
                ('calorific_value', models.CharField(max_length=50, verbose_name='Теплотворная способность')),
                ('ash_content', models.CharField(max_length=50, verbose_name='Зольность')),
                ('strength', models.CharField(max_length=50, verbose_name='Механическая прочность')),
                ('packing', models.CharField(max_length=50, verbose_name='Фасовка')),
                ('price', models.CharField(max_length=50, verbose_name='Цена за тонну')),
                ('picture_main', models.ImageField(unique=True, upload_to='Product/', verbose_name='Освновное фото')),
            ],
        ),
        migrations.CreateModel(
            name='SecondWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=150)),
                ('picture', models.ImageField(upload_to='')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]