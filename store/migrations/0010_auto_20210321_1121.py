# Generated by Django 3.1.5 on 2021-03-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210321_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='websitereport',
            name='report_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='websitereport',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
