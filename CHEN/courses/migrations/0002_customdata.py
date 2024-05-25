# Generated by Django 4.2.6 on 2024-05-25 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio1', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('text1', models.TextField(blank=True, null=True)),
                ('audio2', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('text2', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_data', to='courses.label')),
            ],
        ),
    ]