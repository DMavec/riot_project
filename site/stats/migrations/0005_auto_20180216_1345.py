# Generated by Django 2.0.2 on 2018-02-16 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20180215_1309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
        migrations.RenameModel(
            old_name='Players',
            new_name='Player',
        ),
    ]
