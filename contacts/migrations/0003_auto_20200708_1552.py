# Generated by Django 3.0.8 on 2020-07-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200707_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]