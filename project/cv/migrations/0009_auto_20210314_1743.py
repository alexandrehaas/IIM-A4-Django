# Generated by Django 3.1.7 on 2021-03-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_auto_20210311_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
