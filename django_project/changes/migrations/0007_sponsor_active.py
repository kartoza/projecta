# Generated by Django 2.2 on 2019-12-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0006_auto_20191219_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Check if this sustaining member is active'),
        ),
    ]
