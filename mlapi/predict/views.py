import pandas as pd

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import models, serializers
from ml_model import settings


class PredictView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        features_serializer = serializers.FeatureSerializer(data=request.data, many=True)

        if features_serializer.is_valid():
            features_objects = features_serializer.save()
            features_df = to_dataframe(features_serializer.data)

            preprocessed = preprocessing(features_df)
            predictions = settings.ML_MODEL.predict(preprocessed[settings.FEATURES_COLUMNS])

            for feature, pred in zip(features_objects, predictions):
                prediction = models.Prediction(prediction=pred, feature=feature)
                prediction.save()

            return Response(predictions)

        else:
            return Response(features_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def to_dataframe(features):
    features_df = pd.DataFrame(features)
    for column in settings.DATE_COLUMNS:
        features_df[column] = pd.to_datetime(features_df[column])

    for column in settings.CATEGORY_COLUMNS:
        features_df[column] = features_df[column].astype('category')

    return features_df


def preprocessing(data):
    preprocessed = data.copy()

    for date_column in settings.DATE_COLUMNS:
        # Check NaT values and convert them to timestamp
        preprocessed[date_column] = preprocessed[date_column].apply(
            lambda x: settings.NULL_DATE_VALUE.timestamp()
            if x is pd.NaT else x.timestamp())

    for category_column in settings.CATEGORY_COLUMNS:
        # Check NaN values and convert them to NULL_CATEGORY_KEY
        preprocessed[category_column] = preprocessed[category_column].cat \
            .add_categories(settings.NULL_CATEGORY_KEY) \
            .fillna(settings.NULL_CATEGORY_KEY)

    for number_column in settings.NUMBER_COLUMNS:
        # Check NaN values and convert them to NULL_NUMBER_VALUE
        preprocessed[number_column] = preprocessed[number_column].apply(
            lambda x: settings.NULL_NUMBER_VALUE if pd.isna(x) else x)

    preprocessed[settings.CREDIT_CARD_COLUMN] = data[settings.CREDIT_CARD_COLUMN].apply(get_credit_card_id)
    preprocessed[settings.AFF_TYPE_COLUMN] = data[settings.AFF_TYPE_COLUMN].apply(get_aff_type_id)
    preprocessed[settings.COUNTRY_SEGMENT_COLUMN] = data[settings.COUNTRY_SEGMENT_COLUMN].apply(get_country_id)

    return preprocessed


def get_credit_card_id(credit_card):
    obj, _ = models.CreditCard.objects.get_or_create(type=credit_card)
    return obj.id


def get_aff_type_id(aff_type):
    obj, _ = models.AffType.objects.get_or_create(type=aff_type)
    return obj.id


def get_country_id(country_segment):
    obj, _ = models.Country.objects.get_or_create(code=country_segment)
    return obj.id

