from django.db import models
import json
from .constants import *
from datetime import datetime

# Classes to be used by model Classes
class Location(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    @staticmethod
    def createFromJsonDict(jsonDict):
        return Location(jsonDict['lat'], jsonDict['lng'])


class GroceryStoreItem(object):
    def __init__(self, item_name, notes):
        self.item_name = item_name
        self.notes = notes

    @staticmethod
    def createFromJsonDict(jsonDict):
        return GroceryStoreItem(jsonDict['item_name'], jsonDict['notes'])


# Create your models here.
class VolunteerUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    total_deliveries = models.IntegerField(default=0)
    is_allowed_to_use_app = models.BooleanField(default=True)
    strikes = models.IntegerField(default=0)
    profile_image_ref = models.CharField(max_length=100, default='')
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
            'id': volunteerUser.id,
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

class ClientUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    total_orders = models.IntegerField(default=0)
    is_allowed_to_use_app = models.BooleanField(default=True)
    strikes = models.IntegerField(default=0)
    profile_image_ref = models.CharField(max_length=50, default='')
    address = models.TextField()
    address_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @staticmethod
    def convertToJsonDict(clientUser):
        return {
            'id': clientUser.id,
            'first_name': clientUser.first_name,
            'last_name': clientUser.last_name,
            'email': clientUser.email,
            'phone_number': clientUser.phone_number,
            'total_orders': clientUser.total_orders,
            'is_allowed_to_use_app': clientUser.is_allowed_to_use_app,
            'strikes': clientUser.strikes,
            'profile_image_ref': clientUser.profile_image_ref,
            'address': json.loads(clientUser.address),
            'address_name': clientUser.address_name
        }

class LiveGroceryPost(models.Model):
    client_user_id = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    volunteer_user_id = models.ForeignKey(VolunteerUser, on_delete=models.CASCADE)
    grocery_store_address = models.TextField()
    grocery_store_address_name = models.CharField(max_length=50)
    grocery_store_name = models.CharField(max_length=30)
    time_of_grocery_shopping = models.DateTimeField()
    grocery_item_list = models.TextField()
    earliest_time = models.DateTimeField()
    latest_time = models.DateTimeField()
    time_of_post = models.DateTimeField()
    receipt_image_ref = models.CharField(max_length=100, default='')
    grocery_total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    state_of_volunteer = models.CharField(max_length=20)


    def __str__(self):
        return str(self.id)


    @staticmethod
    def convertToJsonDict(liveGroceryPost):
        return {
            "id": liveGroceryPost.id,
            "client_user_id": liveGroceryPost.client_user_id.id,
        	"volunteer_user_id": liveGroceryPost.volunteer_user_id.id,
        	"grocery_store_address": json.loads(liveGroceryPost.grocery_store_address),
        	"grocery_store_address_name": liveGroceryPost.grocery_store_address_name,
        	"grocery_store_name": liveGroceryPost.grocery_store_name,
        	"time_of_grocery_shopping": liveGroceryPost.time_of_grocery_shopping.strftime(dateFormatString),
        	"grocery_item_list": json.loads(liveGroceryPost.grocery_item_list),
        	"earliest_time": liveGroceryPost.earliest_time.strftime(dateFormatString),
        	"latest_time": liveGroceryPost.latest_time.strftime(dateFormatString),
        	"time_of_post":liveGroceryPost.time_of_post.strftime(dateFormatString),
        	"receipt_image_ref": liveGroceryPost.receipt_image_ref,
        	"grocery_total_amount": liveGroceryPost.grocery_total_amount,
        	"state_of_volunteer": liveGroceryPost.state_of_volunteer
        }


class CompletedGroceryPost(models.Model):
    client_user_id = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    volunteer_user_id = models.ForeignKey(VolunteerUser, on_delete=models.CASCADE)
    grocery_store_address = models.TextField()
    grocery_store_address_name = models.CharField(max_length=50)
    grocery_store_name = models.CharField(max_length=30)
    time_of_grocery_shopping = models.DateTimeField()
    grocery_item_list = models.TextField()
    earliest_time = models.DateTimeField()
    latest_time = models.DateTimeField()
    time_of_post = models.DateTimeField()
    receipt_image_ref = models.CharField(max_length=100, default='')
    grocery_total_amount = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return str(self.id)


    @staticmethod
    def convertToJsonDict(liveGroceryPost):
        return {
            "id": liveGroceryPost.id,
            "client_user_id": liveGroceryPost.client_user_id.id,
        	"volunteer_user_id": liveGroceryPost.volunteer_user_id.id,
        	"grocery_store_address": json.loads(liveGroceryPost.grocery_store_address),
        	"grocery_store_address_name": liveGroceryPost.grocery_store_address_name,
        	"grocery_store_name": liveGroceryPost.grocery_store_name,
        	"time_of_grocery_shopping": liveGroceryPost.time_of_grocery_shopping.strftime(dateFormatString),
        	"grocery_item_list": json.loads(liveGroceryPost.grocery_item_list),
        	"earliest_time": liveGroceryPost.earliest_time.strftime(dateFormatString),
        	"latest_time": liveGroceryPost.latest_time.strftime(dateFormatString),
        	"time_of_post":liveGroceryPost.time_of_post.strftime(dateFormatString),
        	"receipt_image_ref": liveGroceryPost.receipt_image_ref,
        	"grocery_total_amount": liveGroceryPost.grocery_total_amount,
        }
