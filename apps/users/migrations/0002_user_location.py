# Generated by Django 5.0.6 on 2024-06-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
