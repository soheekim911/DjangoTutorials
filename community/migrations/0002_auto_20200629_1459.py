# Generated by Django 3.0.7 on 2020-06-29 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='contents',
            new_name='content',
        ),
    ]