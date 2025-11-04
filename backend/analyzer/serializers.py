from rest_framework import serializers
from .models import GovernmentPortal, ScanResult

class ScanResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanResult
        fields = '__all__'

class GovernmentPortalSerializer(serializers.ModelSerializer):
    latest_scan = serializers.SerializerMethodField()
    
    def get_latest_scan(self, obj):
        latest = obj.scan_results.first()
        return ScanResultSerializer(latest).data if latest else None

    class Meta:
        model = GovernmentPortal
        fields = '__all__'
        