import json
from .models import *
import geopy.distance

def writeVolunteerUserToDatabaseFromRequest(request, id=None):
    # get the request body and convert it to python dict object
    body_dict = json.loads(request.body)

    # Serialize address and preferred_grocery_stores to strings
    user_address_string = json.dumps(body_dict['address'])
    preferred_grocery_stores_string = json.dumps(body_dict['preferred_grocery_stores'])

    # Create the VolunteerUser object and save it to database
    volunteerUser = VolunteerUser(
        first_name = body_dict['first_name'],
        last_name = body_dict['last_name'],
        email = body_dict['email'],
        phone_number = body_dict['phone_number'],
        total_deliveries = body_dict['total_deliveries'],
        is_allowed_to_use_app = body_dict['is_allowed_to_use_app'],
        strikes = body_dict['strikes'],
        profile_image_ref = body_dict['profile_image_ref'],
        address = user_address_string,
        preferred_grocery_stores = preferred_grocery_stores_string,
        get_store_notifications =  body_dict['get_store_notifications'],
    )

    if id != None:
        volunteerUser.id = id

    volunteerUser.save()


def get_kilometer_distance_between_two_points(lat1, long1, lat2, long2):
    coords_1 = (lat1, long1)
    coords_2 = (lat2, long2)

    return geopy.distance.distance(coords_1, coords_2).m

def getAllLiveGroceryPosts(isClient, user_id):
    liveGroceryPostList = []

    if(isClient):
        liveGroceryPostList = LiveGroceryPost.objects.filter(client_user_id=user_id)
    else:
        liveGroceryPostList = LiveGroceryPost.objects.filter(volunteer_user_id=user_id)

    liveGroceryPostJsonList = []
    for post in liveGroceryPostList:
        liveGroceryPostJsonList.append(LiveGroceryPost.convertToJsonDict(post))

    return {"result_list": liveGroceryPostJsonList}

def writeClientUserToDatabaseFromRequest(request, id=None):
    # get the request body and convert it to python dict object
    body_dict = json.loads(request.body)

    # Serialize address to strings
    user_address_string = json.dumps(body_dict['address'])

    # Create the ClientUser object and save it to database
    clientUser = ClientUser(
        first_name = body_dict['first_name'],
        last_name = body_dict['last_name'],
        email = body_dict['email'],
        phone_number = body_dict['phone_number'],
        total_orders = body_dict['total_orders'],
        is_allowed_to_use_app = body_dict['is_allowed_to_use_app'],
        strikes = body_dict['strikes'],
        profile_image_ref = body_dict['profile_image_ref'],
        address = user_address_string,
        address_name =  body_dict['address_name'],
    )

    if id != None:
        clientUser.id = id

    clientUser.save()


def getAllComplaints(isVolunteer, user_id):
    complaintsList = []

    if(isVolunteer):
        complaintsList = Complaints.objects.filter(volunteer_user_id=user_id)
    else:
        complaintsList = Complaints.objects.filter(client_user_id=user_id)

    complaintsJsonList = []
    for post in complaintsList:
        complaintsJsonList.append(Complaints.convertToJsonDict(post))

    return {"result_list": complaintsJsonList}
