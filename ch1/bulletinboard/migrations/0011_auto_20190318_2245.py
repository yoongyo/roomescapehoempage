# Generated by Django 2.0.13 on 2019-03-18 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletinboard', '0010_auto_20190318_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bulletinboard.Bulletinboard'),
        ),
    ]
