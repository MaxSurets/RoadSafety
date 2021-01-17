from django.contrib import admin
from maps.models import Accidents, Scores

class AccidentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Accidents, AccidentsAdmin)

class ScoresAdmin(admin.ModelAdmin):
    pass
admin.site.register(Scores, ScoresAdmin)