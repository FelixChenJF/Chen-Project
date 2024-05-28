from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Course)
admin.site.register(Title)
admin.site.register(Label)
admin.site.register(CustomData)
admin.site.register(OSTitle)
admin.site.register(OSLabel)
admin.site.register(OSCustomData)