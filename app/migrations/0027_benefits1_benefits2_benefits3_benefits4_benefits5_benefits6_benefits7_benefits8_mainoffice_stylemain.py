# Generated by Django 2.2.16 on 2020-11-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_applications_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 1',
            },
        ),
        migrations.CreateModel(
            name='Benefits2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 2',
            },
        ),
        migrations.CreateModel(
            name='Benefits3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 3',
            },
        ),
        migrations.CreateModel(
            name='Benefits4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 4',
            },
        ),
        migrations.CreateModel(
            name='Benefits5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 5',
            },
        ),
        migrations.CreateModel(
            name='Benefits6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 6',
            },
        ),
        migrations.CreateModel(
            name='Benefits7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 7',
            },
        ),
        migrations.CreateModel(
            name='Benefits8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('entry', models.TextField(max_length=2000, verbose_name='Запись')),
            ],
            options={
                'verbose_name_plural': 'Приемущества - 8',
            },
        ),
        migrations.CreateModel(
            name='MainOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('link', models.CharField(max_length=1000, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Главный офис',
            },
        ),
        migrations.CreateModel(
            name='StyleMainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно на страницу')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
