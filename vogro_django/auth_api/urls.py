from django.conf.urls import url, include
from django.urls import path
from allauth.account.views import ConfirmEmailView
from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from . import views
from django.contrib.auth import views as contrib_auth_views
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

# PasswordResetView.as_view()

urlpatterns = [
    url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),

    # rest_auth.views URLs 

    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),


    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),

    # contrib_auth_views urls

    path('password_reset/done/', contrib_auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', contrib_auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', contrib_auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # rest_auth registration url
    path('registration/', include('rest_auth.registration.urls')),

    path('resend-verification-email/', views.ResendEmailVerification.as_view(), name='rest_resend_verification_email'),
]