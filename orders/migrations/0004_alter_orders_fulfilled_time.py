# Generated by Django 3.2.7 on 2021-10-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211015_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='fulfilled_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
