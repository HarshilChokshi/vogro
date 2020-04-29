from django.urls import path
from . import views

urlpatterns = [
    path('volunteeruser/<int:user_id>', views.volunteerUser),
    path('volunteeruser/add_user', views.addVolunteerUser),
    path('volunteeruser/match_lat_long', views.launchAllVolunteerUsersMatchingLocationJob),
    path('livegrocerypost/create_post', views.createLiveGroceryPost),
    path('livegrocerypost/volunteeruser/<int:user_id>', views.getAllLiveGroceryPostsByVolunteer),
    path('livegrocerypost/clientuser/<int:user_id>', views.getAllLiveGroceryPostsByClient),
    path('livegrocerypost/attach_receipt/<int:livegrocerypost_id>', views.addReceiptToLiveGroceryPost),
    path('livegrocerypost/<int:livegrocerypost_id>', views.deleteLiveGroceryPost),
]
