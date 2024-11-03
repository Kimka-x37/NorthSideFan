from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='register')
def feed(request):
    return render(request, 'questions/feed.html', {'username':request.user.username})