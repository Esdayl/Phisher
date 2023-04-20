from django.http import HttpResponseRedirect
from django.shortcuts import render
from frontend.models import User

# Modifies link_opened and show the phishing page
def netflix(request,token):
    user = User.objects.get(token=token)
    user.link_opened = 1
    user.save()
    return render(request, 'netflix.html',{'token': token})

def github(request,token):
    user = User.objects.get(token=token)
    user.link_opened = True
    user.save()
    return render(request, 'github.html',{'token': token})

def amazon(request,token):
    user = User.objects.get(token=token)
    user.link_opened = True
    user.save()
    return render(request, 'amazon.html',{'token': token})


# Modifies the db and redirects to the official wesite 

def n_compromised(request,token):
    user = User.objects.get(token=token)
    user.compromised = True
    user.save()
    return HttpResponseRedirect("https://www.netflix.com/fr/login")

def a_compromised(request,token):
    user = User.objects.get(token=token)
    user.compromised = True
    user.save()
    return HttpResponseRedirect("https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Feu.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3Dsgy7Qo4EkHUxdIVyB1MfS8OWxodLSG2CxAOkt2DO_BmZkAAAAAQAAAABkQTtRcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2F%3Fref_%253Datv_unknown%2526mrntrk%253Dslid__pgrid_85154948059_pgeo_9056137_x__adext__ptid_kwd-297838409925&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_fr&openid.mode=checkid_setup&siteState=259-1625619-2283915&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

def g_compromised(request,token):
    user = User.objects.get(token=token)
    user.compromised = True
    user.save()
    return HttpResponseRedirect("https://github.com/login")