# Generated by Django 4.0.3 on 2024-01-14 12:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_rename_body_portfolio_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 12, 56, 14, 186172, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.TimeField(default=datetime.datetime(2024, 1, 14, 12, 56, 14, 189172, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='resume',
            name='response',
        ),
        migrations.AddField(
            model_name='resume',
            name='response',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.resume_responsibility'),
        ),
    ]