from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Participant


class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant


class ParticipantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Participant
    list_display = ["__str__", "email", "institution", "mobile", "event"]
    list_filter = ["institution", "yos_designation", "referralCode", "event"]


admin.site.register(Participant, ParticipantAdmin)
