# Generated by Django 4.2.2 on 2023-09-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0003_alter_review_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="posted_review",
            field=models.BooleanField(default=False),
        ),
    ]
