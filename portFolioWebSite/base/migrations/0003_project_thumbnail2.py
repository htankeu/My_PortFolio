# Generated by Django 4.2.3 on 2023-08-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_project_body_alter_project_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail2',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]