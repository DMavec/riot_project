# Generated by Django 2.0.2 on 2018-03-14 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0012_remove_playersummary_pct_win'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playersummary',
            name='player',
        ),
        migrations.DeleteModel(
            name='PlayerSummary',
        ),
    ]
