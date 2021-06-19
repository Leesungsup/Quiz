# Generated by Django 3.2.3 on 2021-06-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_player_info_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='player_info',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='nation',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='position',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='team',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='value',
            field=models.CharField(max_length=30),
        ),
    ]
