# Generated by Django 2.1.5 on 2019-02-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20190214_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiple_choice',
            name='choice4',
            field=models.CharField(default='choice4', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multiple_choice',
            name='choice5',
            field=models.CharField(default='choice5', max_length=20),
            preserve_default=False,
        ),
    ]