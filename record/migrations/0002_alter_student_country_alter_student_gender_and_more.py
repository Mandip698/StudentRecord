# Generated by Django 4.0.5 on 2022-07-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(choices=[('china', 'China'), ('usa', 'USA'), ('nepal', 'Nepal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='language',
            field=models.CharField(choices=[('chinese', 'Chinese'), ('nepali', 'Nepali'), ('english', 'English')], max_length=50),
        ),
    ]
