from django.contrib import admin

from .models import Schedule, Meeting

admin.site.empty_value_display = "Не задано"


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "start_time",
        "end_time",
        "description",
    )
    list_editable = (
        "start_time",
        "end_time",
    )
    search_fields = ("description",)


class MeetingAdmin(admin.ModelAdmin):
    list_display = (
        "date_time",
        "status",
        "agenda",
    )
    list_editable = ("status",)
    search_fields = ("date_time",)


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Schedule, ScheduleAdmin)
