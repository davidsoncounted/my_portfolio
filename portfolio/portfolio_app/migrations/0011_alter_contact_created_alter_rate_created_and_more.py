# Generated by Django 4.0.3 on 2024-01-15 20:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0010_alter_contact_created_alter_rate_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 20, 29, 39, 530983, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.TimeField(default=datetime.datetime(2024, 1, 15, 20, 29, 39, 544069, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='image',
            field=models.ImageField(blank=True, default='../static/assets/img/avatar.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='resume',
            name='created',
            field=models.TimeField(default=datetime.datetime(2024, 1, 15, 20, 29, 39, 539529, tzinfo=utc)),
        ),
    ]
