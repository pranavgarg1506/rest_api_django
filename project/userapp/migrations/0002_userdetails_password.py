# Generated by Django 3.2.1 on 2021-05-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='password',
            field=models.CharField(default='na', max_length=20),
            preserve_default=False,
        ),
    ]
