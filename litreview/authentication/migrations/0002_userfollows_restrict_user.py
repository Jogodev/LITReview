# Generated by Django 4.2.2 on 2023-08-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userfollows",
            name="restrict_user",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
