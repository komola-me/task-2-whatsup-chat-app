# Generated by Django 4.1 on 2022-08-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]