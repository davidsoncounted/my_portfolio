# Generated by Django 3.2.1 on 2024-01-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0012_rename_host_rate_name_rename_rating_rate_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_details',
            name='cv',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='created',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='response',
            field=models.ManyToManyField(to='portfolio_app.Resume_responsibility'),
        ),
    ]
