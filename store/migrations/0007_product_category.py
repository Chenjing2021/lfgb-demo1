# Generated by Django 3.1.5 on 2021-03-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210317_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Eggs', 'Eggs')], max_length=200, null=True),
        ),
    ]
