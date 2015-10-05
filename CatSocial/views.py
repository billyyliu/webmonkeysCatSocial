from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
def home(request):
    if request.user.is_authenticated():
        #user is logged in and has a valid user account
        return HttpResponseRedirect('/main')
    else:
        return render(request,'landing.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/main')
        else:
            return render(request,'landing.html',{'errors' :'There was a problem with your account, please try logging in again'})
    else:
        return ""

def main(request):
    if not request.user.is_authenticated():
        return render(request,'landing.html')
    else:
        #grab all users
        users = User.objects.all()
        print User.objects.all().query
        userprofiles = UserProfile.objects.filter(user__in=users)
        return render(request, 'main.html', {'userprofiles':userprofiles})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)