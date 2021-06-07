from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import CustomUser,RegisterPerson
from django.views.decorators.csrf import csrf_exempt
from crime_management.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from django.contrib import messages


def showdemopage(request):
    return render(request,"index.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def showlogin_test(request):
    return render(request,"login_test.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>METHOD NOT ALLOWED</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == '1':
                return HttpResponseRedirect('/person_home')
            elif user.user_type == '2':
                return HttpResponseRedirect(reverse("police_home"))
            elif user.user_type == '3':
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == '4':
                return HttpResponseRedirect(reverse("court_home"))
            elif user.user_type == '5':
                return HttpResponseRedirect(reverse("jail_home"))
            elif user.user_type == '6':
                return HttpResponseRedirect(reverse("doctor_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email + " usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please login first")
    
def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

def ViewRegister(request):
    return render(request,'Register.html')

def do_person_register(request):
    name=request.POST.get("Name")
    email=request.POST.get("email")
    nationality=request.POST.get("nationality")
    state=request.POST.get("state")
    Person_DOB=request.POST.get("Person_DOB")
    Person_address=request.POST.get("Person_address")
    Person_Phonenumber=request.POST.get("Person_Phonenumber")
    password=request.POST.get("password")

    try:
        user=CustomUser.objects.create_user(username=name,email=email,password=password,user_type=1)
        user.registerperson.nationality=nationality
        user.registerperson.state=state
        user.registerperson.Person_DOB=Person_DOB
        user.registerperson.address=Person_address
        user.registerperson.phonenumber=Person_Phonenumber
        user.save()
        messages.success(request,"Successfully registered")
        return HttpResponseRedirect("/")
    except:
        messages.error(request,"Failed to register")
        return HttpResponseRedirect("/")
    

    return HttpResponse("Admin User Created")

