# Generated by Django 3.2.7 on 2022-01-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Address',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]