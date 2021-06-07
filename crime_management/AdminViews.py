from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import CustomUser,ChargeSheet
from crime_management.models import Police,Court,Jail,Doctor
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

def admin_home(request):
    polices=Police.objects.all()
    courts=Court.objects.all()
    jails=Jail.objects.all()
    doctors=Doctor.objects.all()
    return render(request,"admin_template/base_template_admin.html",{"polices":polices,"courts":courts,"jails":jails,"doctors":doctors})

def add_police(request):
    return render(request,"admin_template/add_police.html")

def add_police_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        officer_name=request.POST.get("officer_name")
        officer_address=request.POST.get("officer_address")
        officer_phonenumber=request.POST.get("officer_phonenumber")
        officer_email=request.POST.get("officer_email")
        officer_password=request.POST.get("officer_password")
        officer_DOB=request.POST.get("officer_DOB")
        officer_sex=request.POST.get("officer_sex")
        officer_rank=request.POST.get("officer_rank")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'officer_image' in doc:
            officer_image = doc['officer_image']
            filename1 = fs.save(officer_image.name,officer_image)
            officer_image_url = fs.url(filename1)
        else:
            officer_image_url = None

        try:
            user=CustomUser.objects.create_user(username=officer_name,email=officer_email,password=officer_password,user_type=2)
            user.police.address=officer_address
            user.police.phonenumber=officer_phonenumber
            user.police.position=officer_rank
            user.police.Sex=officer_sex
            user.police.officer_image=officer_image_url
            user.police.DOB=officer_DOB
            user.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_police")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_police")

def remove_police(request):
    pols=Police.objects.all()
    return render(request,"admin_template/remove_police.html",{"pols":pols})

def remove_police_save(request): 
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        police_id = request.POST.get("police_name")

        try:
            police_model=Police.objects.get(admin_id=police_id)
            police_model.delete()
            messages.success(request,"Successfully deleted")
            return HttpResponseRedirect("/remove_police")
        except:
            messages.error(request,"Failed to delete")
            return HttpResponseRedirect("/remove_police")

    return HttpResponse("pol_admin_id :"+ rem_police_id)

def view_police(request):
    pols=Police.objects.all()
    return render(request,"admin_template/view_edit_police.html",{"pols":pols})

def edit_police(request,police_id):
    police=Police.objects.get(admin_id=police_id)
    return render(request,"admin_template/edit_police.html",{"police":police})

def edit_police_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        police_id=request.POST.get("police_id")
        officer_name=request.POST.get("officer_name")
        officer_address=request.POST.get("officer_address")
        officer_phonenumber=request.POST.get("officer_phonenumber")
        officer_email=request.POST.get("officer_email")
        officer_DOB=request.POST.get("officer_DOB")
        officer_sex=request.POST.get("officer_sex")
        officer_rank=request.POST.get("officer_rank")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'officer_image' in doc:
            officer_image = doc['officer_image']
            filename1 = fs.save(officer_image.name,officer_image)
            officer_image_url = fs.url(filename1)

        try:
            police_model=Police.objects.get(admin_id=police_id)
            police_model.admin.name=officer_name
            police_model.admin.email=officer_email
            police_model.address=officer_address
            police_model.phonenumber=officer_phonenumber
            police_model.position=officer_rank
            police_model.DOB=officer_DOB
            police_model.Sex=officer_sex

            if officer_image_url != None:
                police_model.officer_image=officer_image_url

            police_model.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/edit_police/"+str(police_id))
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_police/"+str(police_id))


def add_court(request):
    return render(request,"admin_template/add_court.html")

def add_court_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:        
        court_name=request.POST.get("court_name")
        court_email=request.POST.get("court_email")
        court_password=request.POST.get("court_password")
        court_type=request.POST.get("court_type")
        court_address=request.POST.get("court_address")
        court_phonenumber=request.POST.get("court_phonenumber")

        try:
            user=CustomUser.objects.create_user(username=court_name,email=court_email,password=court_password,user_type=4)
            user.court.address=court_address
            user.court.phonenumber=court_phonenumber
            user.court.court_type=court_type
            user.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_court")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_court")

def remove_court(request):
    courts=Court.objects.all()
    return render(request,"admin_template/remove_court.html",{"courts":courts})

def remove_court_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        court_id = request.POST.get("court_name")

        try:
            court_model=Court.objects.get(admin_id=court_id)
            court_model.delete()
            messages.success(request,"Successfully deleted")
            return HttpResponseRedirect("/remove_court")
        except:
            messages.error(request,"Failed to delete")
            return HttpResponseRedirect("/remove_court")

def view_courts(request):
    courts=Court.objects.all()
    return render(request,"admin_template/view_courts.html",{"courts":courts})

def edit_court(request,court_id):
    court=Court.objects.get(admin_id=court_id)
    return render(request,"admin_template/edit_court.html",{"court":court})

def edit_court_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        court_id=request.POST.get("court_id")
        court_name=request.POST.get("court_name")
        court_address=request.POST.get("court_address")
        court_phonenumber=request.POST.get("court_phonenumber")
        court_email=request.POST.get("court_email")
        court_type=request.POST.get("court_type")

        try:
            court_model=Court.objects.get(admin_id=court_id)
            court_model.admin.name=court_name
            court_model.admin.email=court_email
            court_model.address=court_address
            court_model.phonenumber=court_phonenumber
            court_model.court_type=court_type
            court_model.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/edit_court/"+str(court_id))
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_court/"+str(court_id))

def add_jail(request):
    return render(request,"admin_template/add_jail.html")

def add_jail_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        jail_name=request.POST.get("jail_name")
        jail_email=request.POST.get("jail_email")
        jail_password=request.POST.get("jail_password")
        jail_address=request.POST.get("jail_address")
        jail_phonenumber=request.POST.get("jail_phonenumber")
        jailer=request.POST.get("jailer")
        jail_desc=request.POST.get("jail_desc")

        try:
            user=CustomUser.objects.create_user(username=jail_name,email=jail_email,password=jail_password,user_type=5)
            user.jail.jail_name=jail_name
            user.jail.jail_email=jail_email
            user.jail.address=jail_address
            user.jail.phonenumber=jail_phonenumber
            user.jail.jailer=jailer
            user.jail.description=jail_desc
            user.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_jail")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_jail")

def remove_jail(request):
    jails=Jail.objects.all()
    return render(request,"admin_template/remove_jail.html",{"jails":jails})

def remove_jail_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        jail_id = request.POST.get("jail_name")

        try:
            jail_model=Jail.objects.get(admin_id=jail_id)
            jail_model.delete()
            messages.success(request,"Successfully deleted")
            return HttpResponseRedirect("/remove_jail")
        except:
            messages.error(request,"Failed to delete")
            return HttpResponseRedirect("/remove_jail")

def view_jail(request):
    jails=Jail.objects.all()
    return render(request,"admin_template/view_jail.html",{"jails":jails})

def edit_jail(request,jail_id):
    jail=Jail.objects.get(admin_id=jail_id)
    return render(request,"admin_template/edit_jail.html",{"jail":jail})

def edit_jail_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        jail_id=request.POST.get("jail_id")
        jail_name=request.POST.get("jail_name")
        jail_address=request.POST.get("jail_address")
        jail_phonenumber=request.POST.get("jail_phonenumber")
        jail_email=request.POST.get("jail_email")
        jail_jailer=request.POST.get("jail_jailer")
        jail_description=request.POST.get("jail_description")

        try:
            jail_model=Jail.objects.get(admin_id=jail_id)
            jail_model.admin.name=jail_name
            jail_model.admin.email=jail_email
            jail_model.address=jail_address
            jail_model.phonenumber=jail_phonenumber
            jail_model.jailer=jail_jailer
            jail_model.description=jail_description
            jail_model.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/edit_jail/"+str(jail_id))
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_jail/"+str(jail_id))


def add_doctor(request):
    return render(request,"admin_template/add_doctor.html")

def add_doctor_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        doctor_name=request.POST.get("doctor_name")
        doctor_email=request.POST.get("doctor_email")
        doctor_password=request.POST.get("doctor_password")
        doctor_sex=request.POST.get("doctor_sex")
        doctor_address=request.POST.get("doctor_address")
        doctor_phonenumber=request.POST.get("doctor_phonenumber")
        doctor_DOB=request.POST.get("doctor_DOB")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'doctor_image' in doc:
            doctor_image = doc['doctor_image']
            filename1 = fs.save(doctor_image.name,doctor_image)
            doctor_image_url = fs.url(filename1)
        else:
            doctor_image_url = None

        try:
            user=CustomUser.objects.create_user(username=doctor_name,email=doctor_email,password=doctor_password,user_type=6)
            user.doctor.address=doctor_address
            user.doctor.phonenumber=doctor_phonenumber
            user.doctor.DOB=doctor_DOB
            user.doctor.sex=doctor_sex
            user.doctor.image=doctor_image_url
            user.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_doctor")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_doctor")

def remove_doctor(request):
    doctors=Doctor.objects.all()
    return render(request,"admin_template/remove_doctor.html",{"doctors":doctors})

def remove_doctor_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        doctor_id = request.POST.get("doctor_name")

        try:
            doctor_model=Doctor.objects.get(admin_id=doctor_id)
            doctor_model.delete()
            messages.success(request,"Successfully deleted")
            return HttpResponseRedirect("/remove_doctor")
        except:
            messages.error(request,"Failed to delete")
            return HttpResponseRedirect("/remove_doctor")

def view_doctor(request):
    doctors=Doctor.objects.all()
    return render(request,"admin_template/view_doctor.html",{"doctors":doctors})

def edit_doctor(request,doctor_id):
    doctor=Doctor.objects.get(admin_id=doctor_id)
    return render(request,"admin_template/edit_doctor.html",{"doctor":doctor})

def edit_doctor_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        doctor_id=request.POST.get("doctor_id")
        doctor_name=request.POST.get("doctor_name")
        doctor_address=request.POST.get("doctor_address")
        doctor_phonenumber=request.POST.get("doctor_phonenumber")
        doctor_email=request.POST.get("doctor_email")
        doctor_sex=request.POST.get("doctor_sex")
        doctor_DOB=request.POST.get("doctor_DOB")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'doctor_image' in doc:
            doctor_image = doc['doctor_image']
            filename1 = fs.save(doctor_image.name,doctor_image)
            doctor_image_url = fs.url(filename1)

        try:
            doctor_model=Doctor.objects.get(admin_id=doctor_id)
            doctor_model.admin.name=doctor_name
            doctor_model.admin.email=doctor_email
            doctor_model.doctor_name=doctor_name
            doctor_model.doctor_email=doctor_email
            doctor_model.address=doctor_address
            doctor_model.phonenumber=doctor_phonenumber
            doctor_model.sex=doctor_sex
            doctor_model.DOB=doctor_DOB

            if doctor_image_url != None:
                doctor_model.image=doctor_image_url
            doctor_model.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/edit_doctor/"+str(doctor_id))
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_doctor/"+str(doctor_id))

