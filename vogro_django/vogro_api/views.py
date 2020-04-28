from .models import *
from .view_helpers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
            setattr(volunteerUser, field_name, field_new_value)
        volunteerUser.save()
        return HttpResponse('Successfully updated VolunteerUser object', status=200)
    else:
        return HttpResponse('Only the GET and PUT verbs can be used on this endpoint.', status=405)


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
