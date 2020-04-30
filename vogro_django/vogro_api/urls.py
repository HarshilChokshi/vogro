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
    path('clientuser/<int:user_id>', views.clientUser),
    path('clientuser/add_user', views.addClientUser),
    path('completedgrocerypost/create_post', views.createCompletedGroceryPost),
    path('completedgrocerypost/volunteeruser/<int:user_id>', views.getAllCompletedGroceryPostsByVolunteer),
    path('completedgrocerypost/clientuser/<int:user_id>', views.getAllCompletedGroceryPostsByVolunteer),
]
