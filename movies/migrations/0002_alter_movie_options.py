# Generated by Django 4.2.6 on 2023-10-23 15:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"ordering": ["title", "release_date", "genre"]},
        ),
    ]
