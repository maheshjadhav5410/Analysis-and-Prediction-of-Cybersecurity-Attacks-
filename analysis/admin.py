from django.contrib import admin
from .models import CyberThreat

@admin.register(CyberThreat)
class CyberThreatAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'source_ip', 'destination_ip', 'attack_type', 'severity_level')
    search_fields = ('source_ip', 'destination_ip', 'attack_type', 'severity_level')
