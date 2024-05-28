from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.courseName

class Title(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

class OSTitle(models.Model):
    id = models.AutoField(primary_key=True)
    OSTitle = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.OSTitle

class Label(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=200, null=True)
    title = models.ForeignKey(Title, related_name='labels', on_delete=models.CASCADE)

    def __str__(self):
        return self.label
    
class OSLabel(models.Model):
    id = models.AutoField(primary_key=True)
    OSLabel = models.CharField(max_length=200, null=True)
    OSTitle = models.ForeignKey(OSTitle, related_name='OS_labels', on_delete=models.CASCADE)

    def __str__(self):
        return self.OSLabel
class CustomData(models.Model):
    id = models.AutoField(primary_key=True)
    text1 = models.TextField(max_length=100000, null=True, blank=True)
    text2 = models.TextField(max_length=100000, null=True, blank=True)
    message = models.TextField(max_length=100000, null=True, blank=True)
    label = models.ForeignKey(Label, related_name='custom_data', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text1
    

class OSCustomData(models.Model):
    id = models.AutoField(primary_key=True)
    OSText = models.TextField(max_length=100000, null=True, blank=True)
    OSImage = models.ImageField(upload_to='OScustom_images/', null=True, blank=True)
    OSLabel = models.ForeignKey(OSLabel, related_name='OScustom_data', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.OSText
    
    
    