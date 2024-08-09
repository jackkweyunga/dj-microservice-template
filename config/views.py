"""
Root views
"""
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from config import VERSION, BUILD


class HealCheck(APIView):
    """
    Application healthcheck endpoint.

    /healthcheck

    """

    def get(self, request, *args, **kwargs):
        return Response({
            "now": f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')}",
            "status": "healthy",
            "version": VERSION,
            "build": BUILD
        }, status=status.HTTP_200_OK)
    