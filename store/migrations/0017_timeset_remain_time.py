# Generated by Django 3.1.5 on 2021-04-06 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210405_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeset',
            name='Remain_time',
            field=models.TimeField(max_length=100, null=True),
        ),
    ]
