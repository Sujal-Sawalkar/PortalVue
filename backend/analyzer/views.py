from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import GovernmentPortal, ScanResult
from .serializers import GovernmentPortalSerializer, ScanResultSerializer
from .analyzers import scan_website
from django.utils import timezone
import threading

class GovernmentPortalViewSet(viewsets.ModelViewSet):
    queryset = GovernmentPortal.objects.all()
    serializer_class = GovernmentPortalSerializer
    
    @action(detail=True, methods=['post'])
    def scan(self, request, pk=None):
        portal = self.get_object()
        
        def run_scan():
            try:
                result = scan_website(portal.url)
                
                ScanResult.objects.create(
                    portal=portal,
                    accessibility_score=result['accessibility'],
                    security_score=result['security'],
                    performance_score=result['performance'],
                    code_quality_score=result['code_quality'],
                    accessibility_issues={'issues': result['issues']},
                    security_issues={},
                    performance_data={},
                    code_quality_issues={},
                    ai_recommendations=result['ai_recommendations']
                )
                
                portal.last_scanned = timezone.now()
                portal.save()
                
            except Exception as e:
                print(f"Error: {e}")
        
        thread = threading.Thread(target=run_scan)
        thread.daemon = True
        thread.start()
        
        return Response({'status': 'Scan started'}, status=202)

class ScanResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer