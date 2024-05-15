from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'birthday',
    )    


admin.site.register(Birthday, BirthdayAdmin)
