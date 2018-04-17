from django.contrib import admin
from .models import Dimension, Criteria, Assessment, AssessmentAnswer

# Register your models here.

class DimensionAdmin(admin.ModelAdmin):
    fields = ['dimension_name', 'dimension_description']

class CriteriaAdmin(admin.ModelAdmin):
    list_display = ('criteria_name', 'dimension')

admin.site.register(Dimension)
admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(Assessment)
admin.site.register(AssessmentAnswer)