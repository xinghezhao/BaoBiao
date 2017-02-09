from django.shortcuts import render
from django.http import HttpResponse #指定返回给用户的类型
import json
from itertools import zip_longest


from .models import UserMessage
# Create your views here.

def to_index(request):
    if request.is_ajax():
        if request.method == 'GET':
            pass

        elif request.method == 'POST':

            center_number = request.POST.get('center_number', '')
            center_mc = request.POST.get('center_mc', '')
            center_pr = request.POST.get('center_pr', '')
            center_mobile = request.POST.get('center_mobile', '')
            sscx_select = request.POST.get('sscx_select', '')
            start_time = request.POST.get('start_time', '')

            user_message = UserMessage()
            user_message.center_number = center_number
            user_message.center_mc = center_mc
            user_message.center_pr = center_pr
            user_message.center_mobile = center_mobile
            user_message.address = sscx_select
            user_message.start_time = start_time
            user_message.save()

    return render(request, 'index.html', {})


def to_message(request):
    if request.is_ajax():
        if request.method == 'GET':
            pass

        elif request.method == 'POST':

            all_messages = UserMessage.objects.all()

            a_Number = []
            for message in all_messages:
                a_Number.append(message.center_number)
            a_Person = []
            for message in all_messages:
                a_Person.append(message.center_pr)
            a_Mobile = []
            for message in all_messages:
                a_Mobile.append(message.center_mobile)
            a_Address = []
            for message in all_messages:
                a_Address.append(message.address)
            a_Time = []
            for message in all_messages:
                a_Time.append(message.start_time)

            for i in zip_longest(a_Number,a_Person,a_Mobile,a_Address,a_Time):
                    print (i)

            # All = [
            #     a_Number,
            #     a_Person,
            #     a_Mobile,
            #     a_Address,
            #     a_Time
            # ]



    return HttpResponse(json.dumps(All), content_type="application/json")



def to_login(request):
    return render(request, 'login.html',{})