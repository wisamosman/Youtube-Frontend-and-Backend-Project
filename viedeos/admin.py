from django.contrib import admin
from .models import Video , Author , Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'



admin.site.register(Video,SomeModelAdmin)
admin.site.register(Author)
admin.site.register(Review)
