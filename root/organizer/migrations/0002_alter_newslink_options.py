# Generated by Django 4.2.3 on 2023-07-17 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newslink',
            options={'get_latest_by': 'pub_date', 'ordering': ['-pub_date'], 'verbose_name': 'News Article'},
        ),
    ]
