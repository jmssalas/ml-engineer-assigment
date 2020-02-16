from rest_framework import serializers
from models.models import Feature, Prediction, Country, AffType, CreditCard


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id']


class AffTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffType
        fields = ['id']


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id']
