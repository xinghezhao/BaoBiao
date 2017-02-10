import json
import datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse #指定返回给用户的类型
from itertools import zip_longest


from .models import UserMessage
# Create your views here.

def to_index(request):
    if request.is_ajax():
        if request.method == 'GET':
            pass

        elif request.method == 'POST':
            id = request.POST.get('id', '')
            center_number = request.POST.get('center_number', '')
            center_mc = request.POST.get('center_mc', '')
            center_pr = request.POST.get('center_pr', '')
            center_mobile = request.POST.get('center_mobile', '')
            sscx_select = request.POST.get('sscx_select', '')
            start_time = request.POST.get('start_time', '')
            start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')

            if not id.strip()=='':

                UserMessage.objects.get(id=id).delete()


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
                    'model_cname': msg.center_mc,
                    'model_name': msg.center_pr,
                    'model_phone': msg.center_mobile,
                    'model_address':msg.address,
                    'model_time':msg.start_time.strftime('%Y-%m-%d %H:%M:%S')
                }
                data_list.append(item)

        return HttpResponse(json.dumps(data_list), content_type="application/json")




def center_detail(request):
    if request.is_ajax():
        if request.method == 'POST':
            ID = request.POST.get('id', '')
            msg = UserMessage.objects.get(id = ID)


            item = {
                'id': msg.id,
                'model_number': msg.center_number,
                'model_cname': msg.center_mc,
                'model_name': msg.center_pr,
                'model_phone': msg.center_mobile,
                'model_address': msg.address,
                'model_time': msg.start_time.strftime('%Y-%m-%d %H:%M:%S')
            }

        return HttpResponse(json.dumps(item), content_type="application/json")





def to_login(request):

    return render(request, 'login.html',{})



def SignIn(request):
    if request.is_ajax:
        if request.method == 'POST':
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password','')

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponse('{"status":"success"}', content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail"}', content_type='application/json')



def Logout(request):
    """
    用户登出
    """
    if request.is_ajax:
        if request.method == 'POST':
            l_close = request.POST.get('logout','')
            if l_close == 'abc':

                logout(request)
                return HttpResponse('{"status":"success"}', content_type='application/json')