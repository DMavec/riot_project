# Generated by Django 2.0.2 on 2018-03-13 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_auto_20180313_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameattribute',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='playersummary',
            old_name='games',
            new_name='n_games',
        ),
        migrations.RenameField(
            model_name='playersummary',
            old_name='wins',
            new_name='n_wins',
        ),
        migrations.RenameField(
            model_name='playersummary',
            old_name='win_rate',
            new_name='pct_win',
        ),
    ]
