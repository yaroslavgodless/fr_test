# Generated by Django 3.2.8 on 2021-10-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='user_id',
            field=models.CharField(blank=True, max_length=30, verbose_name='ID пользователя'),
        ),
    ]