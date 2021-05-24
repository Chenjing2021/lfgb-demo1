# Generated by Django 3.1.5 on 2021-04-06 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210328_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_time', models.DateTimeField(max_length=100, null=True)),
                ('End_time', models.DateTimeField(max_length=100, null=True)),
                ('Delivery_date', models.DateField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(null=True),
        ),
    ]
