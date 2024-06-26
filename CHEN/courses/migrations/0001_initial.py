# Generated by Django 4.2.6 on 2024-05-30 09:55

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
            ],
        ),
        migrations.CreateModel(
            name='OSTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('OSTitle', models.CharField(max_length=200, null=True)),
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
            name='OSLabel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('OSLabel', models.CharField(max_length=200, null=True)),
                ('OSTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OS_labels', to='courses.ostitle')),
            ],
        ),
        migrations.CreateModel(
            name='OSCustomData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('OSText', models.TextField(blank=True, max_length=100000, null=True)),
                ('OSImage', models.ImageField(blank=True, null=True, upload_to='OScustom_images/')),
                ('OSLabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OScustom_data', to='courses.oslabel')),
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
