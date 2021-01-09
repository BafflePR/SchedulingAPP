
from django.http import JsonResponse
from django.shortcuts import render
import datetime


# Create your views here.

def index(request,date, time):

    success = {
        'status':200
    }
    
    unsuccessful = {
        'status': 400
    }
    
    datetime_object = datetime.datetime.now()
    
    date_object = date + ' ' + time
    get_date_time = datetime.datetime.strptime(date_object, "%Y/%m/%d %H:%M:%S")

    if datetime_object.year == get_date_time.year:
        if datetime_object.month == get_date_time.month:
            if datetime_object.day == get_date_time.day:
                if datetime_object.hour == get_date_time.hour:
                    if datetime_object.minute == get_date_time.minute:
                        return JsonResponse(success)
                    else: return JsonResponse(unsuccessful)
                else: return JsonResponse(unsuccessful)
            else: return JsonResponse(unsuccessful)
        else: return JsonResponse(unsuccessful)
    else: return JsonResponse(unsuccessful)
    
def status(request):
    stat = {
        'status':'ok'
    }

    return JsonResponse(stat)
