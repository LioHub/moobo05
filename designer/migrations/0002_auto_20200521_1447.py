# Generated by Django 2.2.7 on 2020-05-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='link',
            field=models.URLField(blank=True, default='', max_length=1000, verbose_name='Ссылка на товар'),
        ),
    ]
