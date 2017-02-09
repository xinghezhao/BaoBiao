from django.shortcuts import render
from django.http import HttpResponse #指定返回给用户的类型
import json

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



    return HttpResponse(json.dumps(), content_type="application/json")


def to_login(request):
    return render(request, 'login.html',{})