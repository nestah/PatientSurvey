from django.contrib import admin
from .models import *
# from import_export.admin import ImportExportModelAdmin


admin.site.register(Designation)
admin.site.register(Survey)
admin.site.register(QuestionnaireApi)
admin.site.register(Userlist)
admin.site.register( QuestionnaireTest)

# register excel response tables
# @admin.register(Responses)
# class ViewAdmin(ImportExportModelAdmin):
#      pass
