from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('users/', views.users),
    path('users/me/', views.me)
]

urlpatterns = format_suffix_patterns(urlpatterns)
