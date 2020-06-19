from rest_framework import serializers, viewsets
from .models import Certificate
# Create your views here.


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
