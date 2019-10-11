from django.shortcuts import render
from django.http import JsonResponse
import json
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
    
    if user is not None:
        isSucces = True
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