# Generated by Django 3.2.5 on 2021-07-10 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210710_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
    ]
