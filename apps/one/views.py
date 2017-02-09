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

            data_list = list()
            for msg in all_messages:
                item = {
                    'id': msg.id,
                    'model_number': msg.center_number,
                    'model_name': msg.center_pr,
                    'model_phone': msg.center_mobile,
                    'model_address':msg.address,
                    'model_time':msg.start_time
                }
                data_list.append(item)
                print(data_list)



        return HttpResponse(json.dumps(data_list), content_type="application/json")





def to_login(request):
    return render(request, 'login.html',{})