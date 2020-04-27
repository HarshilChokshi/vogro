from .serializers import *
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


@csrf_exempt
def volunteerUser(request, user_id):
    pass


@csrf_exempt
def addVolunteerUser(request):
    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    if request.content_type != 'application/json':
        return HttpResponse('The content-type must be application/json.', status=415)
    body_dict = json.loads(request.body)
    return HttpResponse("Hello, world.")


@csrf_exempt
def getAllVolunteerUsersMatchingLocation(request):
    pass
