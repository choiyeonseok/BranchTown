# Generated by Django 2.1.5 on 2019-02-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='response_count',
            field=models.IntegerField(default=0),
        ),
    ]
