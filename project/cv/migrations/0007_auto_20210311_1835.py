# Generated by Django 3.1.7 on 2021-03-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20210311_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=320),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='first_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='last_name',
            field=models.CharField(max_length=60),
        ),
    ]
