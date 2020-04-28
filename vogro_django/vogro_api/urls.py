from django.urls import path
from . import views

urlpatterns = [
    path('volunteeruser/<int:user_id>', views.volunteerUser),
    path('volunteeruser/add_user', views.addVolunteerUser),
    path('volunteeruser/match_lat_long', views.launchAllVolunteerUsersMatchingLocationJob),
]
