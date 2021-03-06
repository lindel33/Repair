# Generated by Django 4.0.1 on 2022-01-07 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='cpu',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='repair_home.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='repair_home.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='repair_home.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notebook',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='repair_home.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='repair_home.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocart',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='repair_home.category'),
            preserve_default=False,
        ),
    ]
