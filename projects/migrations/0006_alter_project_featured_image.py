# Generated by Django 5.1.1 on 2024-09-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to=''),
        ),
    ]
