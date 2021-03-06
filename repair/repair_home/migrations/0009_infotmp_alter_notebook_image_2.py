# Generated by Django 4.0.1 on 2022-01-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_home', '0008_notebook_category_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoTmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Марка')),
                ('number_series', models.CharField(max_length=40, verbose_name='Модель\\Серия')),
                ('text', models.TextField(max_length=10000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ноутбук',
                'verbose_name_plural': 'Ноутбуки',
            },
        ),
        migrations.AlterField(
            model_name='notebook',
            name='image_2',
            field=models.ImageField(default='test.jpg', upload_to='media', verbose_name='Фото 2'),
        ),
    ]
