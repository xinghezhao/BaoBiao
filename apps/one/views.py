import json
import datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse #指定返回给用户的类型
from .forms import LoginForm


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

                if request.user.is_authenticated():
                    request_modify = request.user
                    print(request_modify)

                else:
                    pass


                Asingle = UserMessage.objects.get(id=id)
                if not center_number == Asingle.center_number:
                    Asingle.center_number = center_number
                    print(Asingle.center_number)
                    Asingle.save()
                if not center_mc == Asingle.center_mc:
                    Asingle.center_mc = center_mc
                    print(Asingle.center_mc)
                    Asingle.save()
                if not center_pr == Asingle.center_pr:
                    Asingle.center_pr = center_pr
                    Asingle.save()
                if not center_mobile == Asingle.center_mobile:
                    Asingle.center_mobile = center_mobile
                    Asingle.save()
                if not sscx_select == Asingle.address:
                    Asingle.address = sscx_select
                    Asingle.save()
                if not request_modify == Asingle.creator:
                    print(request_modify)
                    print(Asingle.modify_person)
                    Asingle.modify_person = str(request_modify)
                    Asingle.save()

                print(Asingle.change_time)
                if not Asingle.change_time == start_time:

                    Asingle.change_time = start_time
                    Asingle.save()

                return render(request, 'index.html', {})


            user_message = UserMessage()

            if request.user.is_authenticated():
                request_creator = request.user

                print(request_creator)
            else:
                pass

            user_message.creator = request_creator
            user_message.center_number = center_number
            user_message.center_mc = center_mc
            user_message.center_pr = center_pr
            user_message.center_mobile = center_mobile
            user_message.address = sscx_select
            user_message.change_time = start_time
            user_message.start_time = start_time
            user_message.save()

    return render(request, 'index.html', {})


def to_message(request):
    if request.is_ajax():
        if request.method == 'GET':
            pass

        elif request.method == 'POST':

            if not request.user.is_authenticated(): #判断用户是否登录
                return HttpResponse('{"status":"fail"}', content_type='application/json')
            else:
                loginName = str(request.user)
                print(loginName)
            all_messages = UserMessage.objects.all()

            data_list = list()
            for msg in all_messages:
                print(msg.creator.username)
                item = {
                    'id': msg.id,
                    'model_number': msg.center_number,
                    'model_cname': msg.center_mc,
                    'model_name': msg.center_pr,
                    'model_phone': msg.center_mobile,
                    'model_address':msg.address,
                    'model_creater':msg.creator.username,
                    'model_pchange':msg.modify_person,
                    'model_ctime': msg.change_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'model_time':msg.start_time.strftime('%Y-%m-%d %H:%M:%S')
                }
                data_list.append(item)

        data_list = {
            "data_list":data_list,
            'loginName':loginName
        }

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
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user_name = request.POST.get('username','')
                pass_word = request.POST.get('password','')
            else:
                return HttpResponse('{"status":"fail1"}', content_type='application/json')
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