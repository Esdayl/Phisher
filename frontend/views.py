from django.http import HttpResponseRedirect
from django.shortcuts import render
from frontend.models import User

def index(request,token):
    user = User.objects.get(token=token)
    user.link_opened = True
    user.save()
    return render(request, 'login.html',{'token': token})

def adddata(request):
    u1 = User.objects.create(email="u1@test.com",token="u1token")
    u1.save()
    u2 = User.objects.create(email="u2@test.com",token="u2token")
    u2.save()
    u3 = User.objects.create(email="u3@test.com",token="u3token")
    u3.save()
    return render(request,'add.html')

def viewdb(request):
    users = User.objects.all()
    return render(request, 'viewdb.html', {'users': users}) 

def compromised(request,token):
    user = User.objects.get(token=token)
    user.compromised = True
    user.save()
    return HttpResponseRedirect("https://www.netflix.com/fr/login")