from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path(r'^(?P<date>\d{4}/\d{2}/\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})/checkstatus$',views.index, name='index'),
    path('ping/', views.status, name='status')
]