from django.db import models
import json

# Classes to be used by model Classes
class Location(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    @staticmethod
    def createFromJsonDict(jsonDict):
        return Location(jsonDict['lat'], jsonDict['lng'])

# Create your models here.
class VolunteerUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    total_deliveries = models.IntegerField(default=0)
    is_allowed_to_use_app = models.BooleanField(default=True)
    strikes = models.IntegerField(default=0)
    profile_image_ref = models.CharField(max_length=50, default='')
    address = models.TextField()
    preferred_grocery_stores = models.TextField()
    get_store_notifications =  models.BooleanField(default=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @staticmethod
    def createFromJsonDict(jsonDict):
        return VolunteerUser(
            first_name = jsonDict['first_name'],
            last_name = jsonDict['last_name'],
            email = jsonDict['email'],
            phone_number = jsonDict['phone_number'],
            total_deliveries = jsonDict['total_deliveries'],
            is_allowed_to_use_app = jsonDict['is_allowed_to_use_app'],
            strikes = jsonDict['strikes'],
            profile_image_ref = jsonDict['profile_image_ref'],
            address = jsonDict['address'],
            preferred_grocery_stores = jsonDict['preferred_grocery_stores'],
            get_store_notifications = jsonDict['get_store_notifications'],
        )

    @staticmethod
    def convertToJsonDict(volunteerUser):
        return {
            'first_name': volunteerUser.first_name,
            'last_name': volunteerUser.last_name,
            'email': volunteerUser.email,
            'phone_number': volunteerUser.phone_number,
            'total_deliveries': volunteerUser.total_deliveries,
            'is_allowed_to_use_app': volunteerUser.is_allowed_to_use_app,
            'strikes': volunteerUser.strikes,
            'profile_image_ref': volunteerUser.profile_image_ref,
            'address': json.loads(volunteerUser.address),
            'preferred_grocery_stores': json.loads(volunteerUser.preferred_grocery_stores),
            'get_store_notifications': volunteerUser.get_store_notifications
        }
