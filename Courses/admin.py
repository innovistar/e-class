from django.contrib import admin

#from embed_video.admin import AdminVideoMixin
from .models import Course, Topic

# Register your models here.
#class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
#    pass

admin.site.register(Course)
admin.site.register(Topic)
