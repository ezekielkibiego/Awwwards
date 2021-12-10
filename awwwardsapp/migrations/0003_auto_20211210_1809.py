# Generated by Django 3.2.9 on 2021-12-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwardsapp', '0002_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(default='Nairobi', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]