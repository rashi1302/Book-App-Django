# Generated by Django 3.2.5 on 2021-07-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
