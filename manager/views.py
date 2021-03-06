from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import User, Device

def index(request):
    latest_user_list = User.objects.order_by('-join_date')[:5]
    template = loader.get_template('manager/index.html')
    context = {'latest_user_list' : latest_user_list, }
    return HttpResponse(template.render(context, request))
    
def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'manager/detail.html', {'user' : user})
    
def infocheck(request, user_id):
    response = "you're looking at the information of user %s"
    return HttpResponse(response % user_id)
    
def devicecheck(request, user_id):
    return HttpResponse("you're checking devices %s." % user_id)
    
def newuser(request):
    return render(request, 'manager/newuser.html')
    
def addcompleted(request):   
    return render(request, 'manager/addcompleted.html')
    
