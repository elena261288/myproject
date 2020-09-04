# Generated by Django 3.1.1 on 2020-09-04 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onboarding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onboarding.profile')),
            ],
        ),
    ]
