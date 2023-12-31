# Generated by Django 4.2.3 on 2023-11-22 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=datetime.datetime(2023, 11, 22, 18, 49, 6, 333150, tzinfo=datetime.timezone.utc), upload_to='category_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flower',
            name='origin',
            field=models.CharField(default=datetime.datetime(2023, 11, 22, 18, 50, 19, 613260, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flower',
            name='seasonality',
            field=models.CharField(choices=[('all', 'all'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn'), ('Winter', 'Winter')], max_length=20),
        ),
    ]
