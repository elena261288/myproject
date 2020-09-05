# Generated by Django 3.1.1 on 2020-09-04 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0002_auto_20200904_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='id',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='onboarding.profile'),
        ),
    ]
