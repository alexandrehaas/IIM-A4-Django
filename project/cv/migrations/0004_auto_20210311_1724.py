# Generated by Django 3.1.7 on 2021-03-11 16:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20210311_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('html', 'HTML'), ('css', 'CSS'), ('js', 'JavaScript'), ('sass', 'Sass'), ('ts', 'Typescript'), ('react', 'React'), ('angular', 'Angular'), ('vue', 'Vue'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('reactNative', 'React Native'), ('ionic', 'Ionic'), ('php', 'PHP'), ('symfony', 'Symfony'), ('laravel', 'Laravel'), ('drupal', 'Drupal'), ('wordpress', 'Wordpress')], max_length=255),
        ),
    ]
