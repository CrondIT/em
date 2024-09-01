from django.contrib import admin
from .models import Events

# Register your models here.
admin.site.register(Events)
#class NonEditableFields():
#    readonly_fields = ('created_date','updated_date')
