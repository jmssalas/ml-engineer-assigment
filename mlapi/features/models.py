from django.db import models


class Feature(models.Model):
    user_id = models.IntegerField()
    join_date = models.DateTimeField()
    hidden = models.IntegerField(null=True)
    STV = models.FloatField()
    target = models.FloatField()
    credit_card_level = models.CharField(max_length=1000, null=True)
    is_lp = models.IntegerField(null=True)
    aff_type = models.CharField(max_length=1000, null=True)
    is_cancelled = models.IntegerField(null=True)
    country_segment = models.CharField(max_length=1000, null=True)
