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