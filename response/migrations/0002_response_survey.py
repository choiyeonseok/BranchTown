# Generated by Django 2.1.5 on 2019-02-20 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_survey_response_count'),
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
            preserve_default=False,
        ),
    ]
