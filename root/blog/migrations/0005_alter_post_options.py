# Generated by Django 4.2.5 on 2023-09-06 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'pub_date', 'ordering': ['-pub_date', 'title'], 'verbose_name': 'Blog Post'},
        ),
    ]