# Generated by Django 3.2.1 on 2024-01-27 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0014_auto_20240127_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_field', models.FileField(null=True, upload_to='cv_download')),
            ],
        ),
        migrations.RemoveField(
            model_name='resume_details',
            name='cv_field',
        ),
    ]
