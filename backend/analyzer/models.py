from django.db import models

class GovernmentPortal(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    department = models.CharField(max_length=255, default='Government')
    created_at = models.DateTimeField(auto_now_add=True)
    last_scanned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class ScanResult(models.Model):
    portal = models.ForeignKey(GovernmentPortal, on_delete=models.CASCADE, related_name='scan_results')
    scan_date = models.DateTimeField(auto_now_add=True)
    
    accessibility_score = models.IntegerField(default=0)
    security_score = models.IntegerField(default=0)
    performance_score = models.IntegerField(default=0)
    code_quality_score = models.IntegerField(default=0)
    
    accessibility_issues = models.JSONField(default=dict)
    security_issues = models.JSONField(default=dict)
    performance_data = models.JSONField(default=dict)
    code_quality_issues = models.JSONField(default=dict)
    
    ai_recommendations = models.TextField(blank=True)

    def __str__(self):
        return f"{self.portal.name} - {self.scan_date}"