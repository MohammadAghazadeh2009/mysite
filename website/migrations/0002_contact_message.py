# Generated by Django 5.1.6 on 2025-03-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
