# Generated by Django 2.2.16 on 2020-10-22 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201022_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('tell', models.CharField(max_length=13, verbose_name='Телефон')),
                ('mail', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Почта')),
                ('mailing_status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='ProductGalleryVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=5000, verbose_name='Ссылка')),
                ('product', models.ManyToManyField(to='app.Product')),
            ],
            options={
                'verbose_name_plural': 'Ссылки на видео',
            },
        ),
        migrations.CreateModel(
            name='ProductGalleryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ProductImage/', verbose_name='Картинка')),
                ('product', models.ManyToManyField(to='app.Product')),
            ],
            options={
                'verbose_name_plural': 'Фото для товаров',
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Товар', to='app.Product')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]