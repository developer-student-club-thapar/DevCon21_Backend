from django.contrib import admin

from api.models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    model = Participant
    list_display = ["__str__", "email", "institution", "mobile"]
    list_filter = ["institution", "yos_designation", "referralCode"]


admin.site.register(Participant, ParticipantAdmin)
