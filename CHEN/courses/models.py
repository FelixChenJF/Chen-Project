from django.db import models

# Create your models here.

class Course(models.Model):
    from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=200)
    description = models.TextField()
    linkPath = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.courseName

class English(models.Model):
    englishList = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class Label(models.Model):
    english = models.ForeignKey(English, related_name='labels', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.text