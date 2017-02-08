from django.shortcuts import render

# Create your views here.

def to_index(request):
    return render(request, 'index.html',{})