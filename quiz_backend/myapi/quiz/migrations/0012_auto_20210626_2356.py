# Generated by Django 3.2.3 on 2021-06-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_player_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player_info',
            name='photo',
        ),
        migrations.AlterField(
            model_name='player_info',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='nation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='position',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='team',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='value',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player_name',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
