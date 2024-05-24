# Generated by Django 4.2.6 on 2024-05-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_linkpath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='english',
            name='englishList',
        ),
        migrations.AddField(
            model_name='course',
            name='labels',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='english',
            name='label',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='english',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='english',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
