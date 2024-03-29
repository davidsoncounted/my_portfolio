# Generated by Django 4.0.3 on 2024-01-15 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_about_skills_alter_contact_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='aria_level',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 14, 55, 14, 118628, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.TimeField(default=datetime.datetime(2024, 1, 15, 14, 55, 14, 124629, tzinfo=utc)),
        ),
    ]
