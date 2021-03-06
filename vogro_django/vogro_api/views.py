from .models import *
from .view_helpers import *
from .constants import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import operator
from datetime import datetime
from django.db.models import Q
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
            if getMeterDistanceBetweenTwoLocations(lat, long, store['lat'], store['long']) < 100:
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
    earliest_time = datetime.strptime(body_dict['earliest_time'], dateFormatString)
    latest_time = datetime.strptime(body_dict['latest_time'], dateFormatString)

    # Create the LiveGroceryPost object and save to database
    liveGroceryPost = LiveGroceryPost(
        client_user_id_id = body_dict['client_user_id'],
        volunteer_user_id_id = body_dict['volunteer_user_id'],
        grocery_store_address = grocery_address_string,
        grocery_store_address_name = body_dict['grocery_store_address_name'],
        grocery_store_name = body_dict['grocery_store_name'],
        grocery_item_list = grocery_item_list_string,
        earliest_time = earliest_time,
        latest_time = latest_time,
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

    # grab the client user from db
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


@csrf_exempt
def createCompletedGroceryPost(request):
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
    earliest_time = datetime.strptime(body_dict['earliest_time'], dateFormatString)
    latest_time = datetime.strptime(body_dict['latest_time'], dateFormatString)

    # Create the CompletedGroceryPost object and save to database
    completedGrocerypPost = CompletedGroceryPost(
        client_user_id_id = body_dict['client_user_id'],
        volunteer_user_id_id = body_dict['volunteer_user_id'],
        grocery_store_address = grocery_address_string,
        grocery_store_address_name = body_dict['grocery_store_address_name'],
        grocery_store_name = body_dict['grocery_store_name'],
        grocery_item_list = grocery_item_list_string,
        earliest_time = earliest_time,
        latest_time = latest_time,
        receipt_image_ref = body_dict['receipt_image_ref'],
        grocery_total_amount = body_dict['grocery_total_amount'],
    )
    completedGrocerypPost.save()
    return HttpResponse('Successfully added CompletedGroceryPost object', status=200)


@csrf_exempt
def getAllCompletedGroceryPostsByVolunteer(request, user_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    completedGroceryPostJsonDict = getAllCompletedGroceryPosts(False, user_id)
    return JsonResponse(completedGroceryPostJsonDict)

@csrf_exempt
def getAllCompletedGroceryPostsByVolunteer(request, user_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    completedGroceryPostJsonDict = getAllCompletedGroceryPosts(True, user_id)
    return JsonResponse(completedGroceryPostJsonDict)


@csrf_exempt
def createComplaint(request):
    # Make sure request is POST method and content type is application/json
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # get the request body and convert it to python dict object
    body_dict = json.loads(request.body)

    # Create the Complaints object and save to database
    complaints = Complaints(
        client_user_id_id = body_dict['client_user_id'],
        volunteer_user_id_id = body_dict['volunteer_user_id'],
        completed_grocery_post_id_id = body_dict['completed_grocery_post_id'],
        is_complainer_volunteer = body_dict['is_complainer_volunteer'],
        complaint_details = body_dict['complaint_details']
    )
    complaints.save()
    return HttpResponse('Successfully added Complaints object', status=200)


@csrf_exempt
def getComplaintsByVolunteer(request, user_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    complaintsJsonDict = getAllComplaints(True, user_id)
    return JsonResponse(complaintsJsonDict)


@csrf_exempt
def getComplaintsByClient(request, user_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    complaintsJsonDict = getAllComplaints(False, user_id)
    return JsonResponse(complaintsJsonDict)


@csrf_exempt
def createClientGroceryPost(request):
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
    time_of_post = datetime.strptime(body_dict['time_of_post'], dateFormatString)
    earliest_time = datetime.strptime(body_dict['earliest_time'], dateFormatString)
    latest_time = datetime.strptime(body_dict['latest_time'], dateFormatString)

    # Create the CompletedGroceryPost object and save to database
    clientGrocerypPost = ClientGroceryPost(
        client_user_id_id = body_dict['client_user_id'],
        grocery_store_address = grocery_address_string,
        grocery_store_address_name = body_dict['grocery_store_address_name'],
        grocery_store_name = body_dict['grocery_store_name'],
        grocery_item_list = grocery_item_list_string,
        earliest_time = earliest_time,
        latest_time = latest_time,
        time_of_post = time_of_post,
    )
    clientGrocerypPost.save()
    return HttpResponse('Successfully added CientGroceryPost object', status=200)



@csrf_exempt
def getAllClientGroceryPostsBelongingToClient(request, client_id):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # grab all client grocery posts from database
    clientGroceryPostList = ClientGroceryPost.objects.filter(client_user_id=client_id)

    # Convert it to json
    clientGroceryPostJsonList = []
    for post in clientGroceryPostList:
        clientGroceryPostJsonList.append(ClientGroceryPost.convertToJsonDict(post))

    # return json object
    return JsonResponse({"result_list": clientGroceryPostJsonList})


@csrf_exempt
def clientGroceryPost(request, grocery_post_id):
    # Make sure content type is application/json
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # grab the ClientGroceryPost from db
    clientGroceryPost = None
    try:
        clientGroceryPost = ClientGroceryPost.objects.get(id=grocery_post_id)
    except ClientGroceryPost.DoesNotExist:
        return HttpResponse(f'ClientGroceryPost with id: {grocery_post_id}, does not exist', status=404)

    if request.method == 'PATCH':
        # Get the request body
        body_dict = json.loads(request.body)
        fields_to_change_list = body_dict['fields_to_change']

        for field_name, field_new_value in fields_to_change_list.items():
            try:
                getattr(clientGroceryPost, field_name)
            except AttributeError:
                continue
            if field_name == 'grocery_store_address' or field_name == 'grocery_item_list':
                field_new_value = json.dumps(field_new_value)
            elif field_name == 'time_of_post' or \
                    field_name == 'earliest_time' or \
                    field_name == 'latest_time':
                    field_new_value = datetime.strptime(field_new_value, dateFormatString)
            setattr(clientGroceryPost, field_name, field_new_value)
        # Save the object to the database
        clientGroceryPost.save()
        return HttpResponse('Successfully updated ClientGraoceryPost object', status=200)
    elif request.method == 'POST':
        return HttpResponse(f'Successfully deleted ClientGroceryPostObject with id {grocery_post_id}', status=200)
    elif request.method == 'DELETE':
        clientGroceryPost.delete()
        return HttpResponse(f'Successfully deleted ClientGroceryPostObject with id {grocery_post_id}', status=200)
    else:
        return HttpResponse('Only the PATCH, DELETE, or POST verb can be used on this endpoint.', status=405)



@csrf_exempt
def getAllClientGroceryPostNearArea(request):
    # Make sure request is GET method and content type is application/json
    if request.method != 'GET':
        return HttpResponse('Only the GET verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)

    # get the request body and convert it to python dict object
    body_dict = json.loads(request.body)

    # Parse out the time from the body_dict
    volunteerUserEarliestTime = datetime.strptime(body_dict['earliest_time'], dateFormatString)
    volunteerUserLatestTime = datetime.strptime(body_dict['latest_time'], dateFormatString)

    # Parse out lat, longd target radius from dict object
    volunteer_lat = body_dict['lat']
    volunteer_long = body_dict['long']
    radius = body_dict['radius']

    # Parse out the field by which user wants the results to be ordered in
    order_field = body_dict['order_field']

    # Set the time filters for query
    earliestTimeFilter = Q(earliest_time__range=[volunteerUserEarliestTime, volunteerUserLatestTime])
    latestTimeFilter = Q(latest_time__range=[volunteerUserEarliestTime, volunteerUserLatestTime])

    clientGorceryPostsResultSet = []

    # Run the query
    if order_field == 'time_of_post':
        clientGorceryPostsResultSet = ClientGroceryPost.objects.filter(earliestTimeFilter | latestTimeFilter).order_by(order_field)
    else:
        clientGorceryPostsResultSet = ClientGroceryPost.objects.filter(earliestTimeFilter | latestTimeFilter)

    # Filter by specified radius
    clientGorceryPostsRadiusFilterResultTupleSet = []

    for post in clientGorceryPostsResultSet:
        # Parse out the grocery store lat and long
        grocery_store_address_dict = json.loads(post.grocery_store_address)
        store_lat = grocery_store_address_dict['lat']
        store_long = grocery_store_address_dict['long']

        # Get the distance
        distance = getMeterDistanceBetweenTwoLocations(volunteer_lat, volunteer_long, store_lat, store_long)

        # Filter by radius
        if  distance <= radius:
            postTuple = (post, distance)
            clientGorceryPostsRadiusFilterResultTupleSet.append(postTuple)


    # Sort results by distance if needed
    if order_field == 'radius':
        clientGorceryPostsRadiusFilterResultTupleSet.sort(key=operator.itemgetter(1))

    # convert all objects to json and add distance with each object
    clientGroceryPostJsonList = []
    for post in clientGorceryPostsRadiusFilterResultTupleSet:
        post_dict = {}
        post_dict['post'] = ClientGroceryPost.convertToJsonDict(post[0])
        post_dict['distance'] = post[1]
        clientGroceryPostJsonList.append(post_dict)

    # return json object
    return JsonResponse({"result_list": clientGroceryPostJsonList})
