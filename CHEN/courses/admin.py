from django.contrib import admin

# Register your models here.
from .models import Course, Title, Label, CustomData

admin.site.register(Course)
admin.site.register(Title)
admin.site.register(Label)
admin.site.register(CustomData)