# Generated by Django 2.1.5 on 2019-02-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tests', '0012_auto_20190218_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteditem',
            name='note',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
