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
    text1 = models.TextField(max_length=100000, null=True, blank=True)
    text2 = models.TextField(max_length=100000, null=True, blank=True)
    label = models.ForeignKey(Label, related_name='custom_data', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text1
    
class CommentData(models.Model):
    message = models.TextField(max_length=1000, null=True, blank=True)
    label = models.ForeignKey(Label, related_name='comment_data', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message
    
    
    