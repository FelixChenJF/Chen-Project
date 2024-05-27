# Generated by Django 4.2.6 on 2024-05-27 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OSTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('OSTitle', models.CharField(max_length=200, null=True)),
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
    ]
