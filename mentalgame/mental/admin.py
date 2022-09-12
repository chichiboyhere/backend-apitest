from django.contrib import admin
from .models import MentalGameResult, QuantitativeSpsec, VerbalSpsec

# Register your models here.


class MentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'questions', 'speed', 'time')

class QuantitaiveAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'quantitativeSps', 'time')

class VerbalAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'verbalSps', 'time')


admin.site.register(MentalGameResult, MentalAdmin)
admin.site.register(QuantitativeSpsec, QuantitaiveAdmin)
admin.site.register(VerbalSpsec, VerbalAdmin)
