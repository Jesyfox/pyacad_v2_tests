# Generated by Django 2.1.5 on 2019-02-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tests', '0006_auto_20190213_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtestanswers',
            name='question',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
