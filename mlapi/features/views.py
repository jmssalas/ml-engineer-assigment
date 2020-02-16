from rest_framework import generics, permissions
from features.models import Feature
from features.serializers import FeatureSerializer


class FeatureCreate(generics.CreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [permissions.AllowAny]

