# Generated by Django 3.1 on 2020-08-25 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20200806_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ['-at']},
        ),
    ]
