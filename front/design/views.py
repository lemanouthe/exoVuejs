from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def sendregister(request):
    postdata = json.loads(request.body.decode('utf-8'))
    nom = postdata['nom']
    user = postdata['user']
    password = postdata['password']
    repass = postdata['repass']
    email = postdata['email']
    contact = postdata['contact']

    # nom = request.POST.get('nom')
    # user = request.POST.get('user')
    # password = request.POST.get('password')
    # repass = request.POST.get('repass')
    # email = request.POST.get('email')
    # contact = request.POST.get('contact')
    isSucces = False
    cont = 1
    
    if user is not None and nom is not None and password is not None and repass is not None and email is not None and contact is not None:
        isSucces = True
        h = Register(nom=nom,user=user,password=password,repass=repass,email=email,contact=contact)
        h.save()
        print(nom,user,contact,email,password,repass)
    else:
        isSucces = False

    while cont < 100000000:
        cont += 1

    datas = {
        'succes': True,
        'nom': nom,
        'cont': cont
    }
    return JsonResponse(datas, safe=False)

def postimage(request):
    # postdata = json.loads(request.body.decode('utf-8'))
    # nom = postdata['nom']
    # user = postdata['user']
    # password = postdata['password']
    # repass = postdata['repass']
    # email = postdata['email']
    # contact = postdata['contact']
    # image = postdata['file']

    nom = request.POST.get('nom')
    user = request.POST.get('user')
    password = request.POST.get('password')
    repass = request.POST.get('repass')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    
    isSucces = False
    cont = 1
    
    if user is not None and nom is not None and password is not None and repass is not None and email is not None and contact is not None:
        image = request.FILES['file']
        isSucces = True
        h = Register(nom=nom,user=user,password=password,repass=repass,email=email,contact=contact,image=image)
        h.save()
        print(nom,user,contact,email,password,repass,image)
    else:
        isSucces = False

    while cont < 100000000:
        cont += 1

    datas = {
        'succes': True,
        'nom': nom,
        'cont': cont
    }
    return JsonResponse(datas, safe=False)