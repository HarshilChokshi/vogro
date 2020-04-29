from django.conf.urls import url, include
from django.urls import path
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    path('', include('rest_auth.urls')),
]