# Generated by Django 3.2.4 on 2023-01-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]
