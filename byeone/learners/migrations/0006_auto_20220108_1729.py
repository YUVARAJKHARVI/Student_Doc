# Generated by Django 3.2.7 on 2022-01-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learners', '0005_alter_students_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_academics',
            name='Biology',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students_academics',
            name='Chemistry',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students_academics',
            name='English',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students_academics',
            name='Maths',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students_academics',
            name='Physics',
            field=models.IntegerField(),
        ),
    ]
