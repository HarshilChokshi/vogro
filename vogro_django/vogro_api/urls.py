from django.urls import path
from . import views

urlpatterns = [
    # Volunteer user endpoints
    path('volunteeruser/<int:user_id>', views.volunteerUser),
    path('volunteeruser/add_user', views.addVolunteerUser),
    path('volunteeruser/match_lat_long', views.launchAllVolunteerUsersMatchingLocationJob),
    # LiveGroceryPost endpoints
    path('livegrocerypost/create_post', views.createLiveGroceryPost),
    path('livegrocerypost/volunteeruser/<int:user_id>', views.getAllLiveGroceryPostsByVolunteer),
    path('livegrocerypost/clientuser/<int:user_id>', views.getAllLiveGroceryPostsByClient),
    path('livegrocerypost/attach_receipt/<int:livegrocerypost_id>', views.addReceiptToLiveGroceryPost),
    path('livegrocerypost/<int:livegrocerypost_id>', views.deleteLiveGroceryPost),
    # Client user endpoints
    path('clientuser/<int:user_id>', views.clientUser),
    path('clientuser/add_user', views.addClientUser),
    # Complaints endpoints
    path('complaints/create_complaint', views.createComplaint),
    path('complaints/volunteer/<int:user_id>', views.getComplaintsByVolunteer),
    path('complaints/client/<int:user_id>', views.getComplaintsByClient),
    # CompletedGroceryPost endpoints
    path('completedgrocerypost/create_post', views.createCompletedGroceryPost),
    path('completedgrocerypost/volunteeruser/<int:user_id>', views.getAllCompletedGroceryPostsByVolunteer),
    path('completedgrocerypost/clientuser/<int:user_id>', views.getAllCompletedGroceryPostsByVolunteer),
    # MatchedGroceryStore endpoints
    path('clientgrocerypost/create_post', views.createClientGroceryPost),
    path('clientgrocerypost/clientuser/<int:client_id>', views.getAllClientGroceryPostsBelongingToClient),
    path('clientgrocerypost/<int:grocery_post_id>', views.clientGroceryPost),
    path('clientgrocerypost/get_nearby_posts', views.getAllClientGroceryPostNearArea),
]
