# Generated by Django 2.1.5 on 2019-02-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tests', '0004_auto_20190213_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtestanswers',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_tests.Question'),
        ),
    ]
