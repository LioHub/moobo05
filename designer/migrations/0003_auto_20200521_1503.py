# Generated by Django 2.2.7 on 2020-05-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0002_auto_20200521_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='link',
            field=models.URLField(blank=True, default='', max_length=2000, verbose_name='Ссылка на товар'),
        ),
    ]
