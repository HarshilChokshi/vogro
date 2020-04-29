from .models import *
from .view_helpers import *
from .constants import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
# Create your views here.


@csrf_exempt
def volunteerUser(request, user_id):
    # Make sure content type is application/json
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # grab the volunteer user from db
    volunteerUser = None
    try:
        volunteerUser = VolunteerUser.objects.get(id=user_id)
    except VolunteerUser.DoesNotExist:
        return HttpResponse(f'Volunteer user with id: {user_id}, does not exist', status=404)

    # Make sure request is GET, PUT, or PATCH
    if request.method == 'GET':
        volunteerUser_dict = VolunteerUser.convertToJsonDict(volunteerUser)
        return JsonResponse(volunteerUser_dict)
    elif request.method == 'PUT':
        writeVolunteerUserToDatabaseFromRequest(request, id=user_id)
        return HttpResponse('Successfully updated VolunteerUser object', status=200)
    elif request.method == 'PATCH':
        # Get the request body
        body_dict = json.loads(request.body)
        fields_to_change_list = body_dict['fields_to_change']
        for field_name, field_new_value in fields_to_change_list.items():
            try:
                getattr(volunteerUser, field_name)
            except AttributeError:
                continue
            if field_name == 'address' or field_name == 'preferred_grocery_stores':
                field_new_value = json.dumps(field_new_value)
            setattr(volunteerUser, field_name, field_new_value)
        volunteerUser.save()
        return HttpResponse('Successfully updated VolunteerUser object', status=200)
    else:
        return HttpResponse('Only the GET, PUT, and PATCH verbs can be used on this endpoint.', status=405)



@csrf_exempt
def addVolunteerUser(request):
    # Make sure request is POST method and content type is application/json
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)
    writeVolunteerUserToDatabaseFromRequest(request)
    return HttpResponse('Successfully added VolunteerUser object', status=200)



@csrf_exempt
def launchAllVolunteerUsersMatchingLocationJob(request):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the PUT verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # get the request body and convert it to python dict object
    body_dict = json.loads(request.body)

    lat = body_dict['lat']
    long = body_dict['long']

    allVolunteerUsers = VolunteerUser.objects.all()
    targetVolunteerIds = []

    for volunteerUser in allVolunteerUsers:
        grocery_stores_preferred = json.loads(volunteerUser.preferred_grocery_stores)
        for store in grocery_stores_preferred:
            if get_kilometer_distance_between_two_points(lat, long, store['lat'], store['long']) < 100:
                targetVolunteerIds.append(volunteerUser.id)

    return JsonResponse({'target_volunteer_user_ids': targetVolunteerIds})

@csrf_exempt
def createLiveGroceryPost(request):
    # Make sure request is POST method and content type is application/json
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # get the request body and convert it to python dict object
    body_dict = json.loads(request.body)

    # Serialize grocery store address and grocery store item list
    grocery_address_string = json.dumps(body_dict['grocery_store_address'])
    grocery_item_list_string = json.dumps(body_dict['grocery_item_list'])

    # Parse out date and time objects from strings in json
    time_of_grocery_shopping = datetime.strptime(body_dict['time_of_grocery_shopping'], dateFormatString)
    time_of_post = datetime.strptime(body_dict['time_of_post'], dateFormatString)
    earliest_time = datetime.strptime(body_dict['earliest_time'], dateFormatString)
    latest_time = datetime.strptime(body_dict['latest_time'], dateFormatString)

    # Create the LiveGroceryPost object and save to database
    liveGroceryPost = LiveGroceryPost(
        client_user_id_id = body_dict['client_user_id'],
        volunteer_user_id_id = body_dict['volunteer_user_id'],
        grocery_store_address = grocery_address_string,
        grocery_store_address_name = body_dict['grocery_store_address_name'],
        grocery_store_name = body_dict['grocery_store_name'],
        time_of_grocery_shopping = time_of_grocery_shopping,
        grocery_item_list = grocery_item_list_string,
        earliest_time = earliest_time,
        latest_time = latest_time,
        time_of_post = time_of_post,
        receipt_image_ref = body_dict['receipt_image_ref'],
        grocery_total_amount = body_dict['grocery_total_amount'],
        state_of_volunteer = body_dict['state_of_volunteer'],
    )
    liveGroceryPost.save()
    return HttpResponse('Successfully added LiveGroceryPost object', status=200)



@csrf_exempt
def getAllLiveGroceryPostsByVolunteer(request, user_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    liveGroceryPostJsonDict = getAllLiveGroceryPosts(False, user_id)
    return JsonResponse(liveGroceryPostJsonDict)



@csrf_exempt
def getAllLiveGroceryPostsByClient(request, user_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    liveGroceryPostJsonDict = getAllLiveGroceryPosts(True, user_id)
    return JsonResponse(liveGroceryPostJsonDict)


@csrf_exempt
def addReceiptToLiveGroceryPost(request, livegrocerypost_id):
    # Make sure request is PATCH method and content type is application/json
    if request.method != 'PATCH':
        return HttpResponse('Only the PATCH verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)
    # Get the request body
    body_dict = json.loads(request.body)

    try:
        # Grab the LiveGroceryPost object from database
        liveGroceryPost = LiveGroceryPost.objects.get(id=livegrocerypost_id)

        # Grab the new value of the receipt image ref and update value in object
        new_receipt_image_ref = body_dict['new_receipt_image_ref']
        setattr(liveGroceryPost, 'receipt_image_ref', new_receipt_image_ref)
        liveGroceryPost.save()
        return HttpResponse(f'Successfully updated the receipt_image_ref of LiveGroceryPost object with id {livegrocerypost_id}', status=200)
    except KeyError:
        return HttpResponse('The new_receipt_image_ref key must be specified in request body', status=400)
    except LiveGroceryPost.DoesNotExist:
        return HttpResponse(f'LiveGroceryPost user with id: {livegrocerypost_id}, does not exist', status=404)


@csrf_exempt
def deleteLiveGroceryPost(request, livegrocerypost_id):
    # Make sure request is DELETE method and content type is application/json
    if request.method != 'DELETE':
        return HttpResponse('Only the DELETE verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # Grab the LiveGroveryPost object from the db
    try:
        liveGroceryPost = LiveGroceryPost.objects.get(id=livegrocerypost_id)
        liveGroceryPost.delete()
        return HttpResponse(f'Successfully deleted LiveGroceryPost object with id {livegrocerypost_id}', status=200)
    except LiveGroceryPost.DoesNotExist:
        return HttpResponse(f'LiveGroceryPost user with id: {livegrocerypost_id}, does not exist', status=404)

@csrf_exempt
def clientUser(request, user_id):
    # Make sure content type is application/json
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # grab the volunteer user from db
    clientUser = None
    try:
        clientUser = ClientUser.objects.get(id=user_id)
    except ClientUser.DoesNotExist:
        return HttpResponse(f'Client user with id: {user_id}, does not exist', status=404)

    # Make sure request is GET, PUT, or PATCH
    if request.method == 'GET':
        clientUser_dict = ClientUser.convertToJsonDict(clientUser)
        return JsonResponse(clientUser_dict)
    elif request.method == 'PUT':
        writeClientUserToDatabaseFromRequest(request, id=user_id)
        return HttpResponse('Successfully updated ClientUser object', status=200)
    elif request.method == 'PATCH':
        # Get the request body
        body_dict = json.loads(request.body)
        fields_to_change_list = body_dict['fields_to_change']
        for field_name, field_new_value in fields_to_change_list.items():
            try:
                getattr(clientUser, field_name)
            except AttributeError:
                continue
            if field_name == 'address':
                field_new_value = json.dumps(field_new_value)
            setattr(clientUser, field_name, field_new_value)
        clientUser.save()
        return HttpResponse('Successfully updated ClientUser object', status=200)
    else:
        return HttpResponse('Only the GET, PUT and PATCH verbs can be used on this endpoint.', status=405)


@csrf_exempt
def addClientUser(request):
    # Make sure request is POST method and content type is application/json
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)
    writeClientUserToDatabaseFromRequest(request)
    return HttpResponse('Successfully added ClientUser object', status=200)
