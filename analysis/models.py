# cyberthreat\analysis\models.py

from django.db import models

class CyberThreat(models.Model):
    timestamp = models.DateTimeField()
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    source_port = models.IntegerField()
    destination_port = models.IntegerField()
    protocol = models.CharField(max_length=10)
    packet_length = models.IntegerField()
    packet_type = models.CharField(max_length=10)
    traffic_type = models.CharField(max_length=10)
    payload_data = models.TextField()
    malware_indicators = models.BooleanField()
    anomaly_scores = models.FloatField()
    alerts_warnings = models.BooleanField()
    attack_type = models.CharField(max_length=50)
    attack_signature = models.CharField(max_length=255)
    action_taken = models.CharField(max_length=50)
    severity_level = models.CharField(max_length=10)
    user_information = models.CharField(max_length=255)
    device_information = models.CharField(max_length=255)
    network_segment = models.CharField(max_length=50)
    geo_location_data = models.CharField(max_length=255)
    proxy_information = models.BooleanField()
    firewall_logs = models.TextField()
    ids_ips_alerts = models.BooleanField()
    log_source = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.timestamp} - {self.attack_type}'
