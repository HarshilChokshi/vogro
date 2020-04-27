from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.Serializer):
    lat =  serializers.DecimalField(max_digits=8, decimal_places=5)
    long =  serializers.DecimalField(max_digits=8, decimal_places=5)


class VolunteerUserSerializer(serializers.Serializer):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    total_deliveries = models.IntegerField(default=0)
    is_allowed_to_use_app = models.BooleanField(default=True)
    strikes = models.IntegerField(default=0)
    profile_image_ref = models.CharField(max_length=50, blank=True, null=True)
    address = LocationSerializer()
    preferred_grocery_stores = LocationSerializer(many=True)
    get_store_notifications =  models.BooleanField(default=True)
