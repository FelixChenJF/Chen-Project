# Generated by Django 4.2.6 on 2024-05-27 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=200)),
                ('imagePath', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('linkPath', models.CharField(max_length=200, null=True)),
                ('labels', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=200, null=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='courses.title')),
            ],
        ),
        migrations.CreateModel(
            name='CustomData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text1', models.TextField(blank=True, max_length=100000, null=True)),
                ('text2', models.TextField(blank=True, max_length=100000, null=True)),
                ('message', models.TextField(blank=True, max_length=100000, null=True)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_data', to='courses.label')),
            ],
        ),
    ]
