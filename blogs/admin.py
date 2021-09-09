from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Quote)
admin.site.register(Ad)
admin.site.register(About_me)
admin.site.register(Comment)
