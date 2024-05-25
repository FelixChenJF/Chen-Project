from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=200)
    description = models.TextField()
    linkPath = models.CharField(max_length=200, null=True)
    labels = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.courseName

from django.db import models

class Title(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

class Label(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=200, null=True)
    title = models.ForeignKey(Title, related_name='labels', on_delete=models.CASCADE)

    def __str__(self):
        return self.label
class CustomData(models.Model):
    audio1 = models.FileField(upload_to='audios/', null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    audio2 = models.FileField(upload_to='audios/', null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    label = models.ForeignKey(Label, related_name='custom_data', on_delete=models.CASCADE)
    title = models.ForeignKey(Title, related_name='custom_data', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'CustomData - {self.created_at}'