from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import Court,CustomUser,ChargeSheet,Attorney,Judge,Case,Decision,Police,Decision,Jail,Criminal,Release
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
import datetime
import json

def myconverter(o):    
    return o.strftime('%Y-%m-%d')

def court_home(request):
    chargesheets=ChargeSheet.objects.all().filter(status='Pending').count()
    return render(request,"court_template/base_template_court.html",{"chargesheets":chargesheets})

def court_account(request):
    court=Court.objects.get(admin_id=request.user.id)
    return render(request,"court_template/court_account.html",{"court":court})

def court_account_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        court_id=request.POST.get('court_id')
        court_address=request.POST.get('court_address')
        court_phone_number=request.POST.get('court_phone_number')

        try:
            court_model=Court.objects.get(id=court_id)
            court_model.address=court_address
            court_model.phonenumber=court_phone_number
            court_model.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/police_account")
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/police_account")

def view_chargesheets(request):
    chargesheet=ChargeSheet.objects.all()
    cases=Case.objects.all()
    counts=[]
    for i in chargesheet:
        count = 0
        for j in cases:
            if i.id == j.charge_id:
                count += j.id
        if count == 0:
            counts.append('Case Not Filed')
        else:
            counts.append(count)
    countdict=zip(chargesheet,counts)
    return render(request,"court_template/view_chargesheets.html",{"countdict":countdict})

def show_chargesheet(request,charge_id):
    chargesheet=ChargeSheet.objects.get(id=charge_id)
    return render(request,"court_template/show_chargesheet.html",{"chargesheet":chargesheet})

def add_case(request,charge_id):
    chargesheet=ChargeSheet.objects.get(id=charge_id)
    username=request.user.username
    address=request.user.court.address
    court_type=request.user.court.court_type
    attorneys=Attorney.objects.all()
    judges=Judge.objects.all()
    return render(request,"court_template/add_case.html",{"chargesheet":chargesheet,"username":username,"address":address,
    "court_type":court_type,"attorneys":attorneys,'judges':judges})

def add_case_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        charge_id=request.POST.get("charge_id")
        court_name=request.POST.get("court_name")
        court_address=request.POST.get("court_address")
        court_type=request.POST.get("court_type")
        first_hearing=request.POST.get("first_hearing")
        final_hearing=request.POST.get("final_hearing")

        def_att_id=request.POST.get("def_att_id")
        def_att_name=request.POST.get("def_att_name")
        def_att_email=request.POST.get("def_att_email")
        def_att_address=request.POST.get("def_att_address")
        def_att_phonenumber=request.POST.get("def_att_phonenumber")
        def_att_DOB=request.POST.get("def_att_DOB")

        pros_att_id=request.POST.get("pros_att_id")
        pros_att_name=request.POST.get("pros_att_name")
        pros_att_email=request.POST.get("pros_att_email")
        pros_att_address=request.POST.get("pros_att_address")
        pros_att_phonenumber=request.POST.get("pros_att_phonenumber")
        pros_att_DOB=request.POST.get("pros_att_DOB")

        get_judge_id=request.POST.get("get_judge_id")
        judge_name=request.POST.get("judge_name")
        judge_email=request.POST.get("judge_email")
        judge_address=request.POST.get("judge_address")
        judge_phonenumber=request.POST.get("judge_phonenumber")
        judge_DOB=request.POST.get("judge_DOB")

        def_person_name=request.POST.get("def_person_name")
        def_person_email=request.POST.get("def_person_email")
        def_person_address=request.POST.get("def_person_address")
        def_person_phoneno=request.POST.get("def_person_phoneno")
        def_person_DOB=request.POST.get("def_person_DOB")
        def_person_charges=request.POST.get("def_person_charges")
        def_person_crime=request.POST.get("def_person_crime")
        
        pros_person_name=request.POST.get("pros_person_name")
        pros_person_email=request.POST.get("pros_person_email")
        pros_person_address=request.POST.get("pros_person_address")
        pros_person_phoneno=request.POST.get("pros_person_phoneno")
        pros_person_DOB=request.POST.get("pros_person_DOB")
        pros_person_charges=request.POST.get("pros_person_charges")

        chargesheet=ChargeSheet.objects.get(id=charge_id)
        
        fs=FileSystemStorage()
        doc=request.FILES

        if 'def_person_image' in doc:
            def_image = doc['def_person_image']
            filename1 = fs.save(def_image.name,def_image)
            def_image_url = fs.url(filename1)
        else:
            def_image_url = None
        
        if 'pros_person_image' in doc:
            pros_image = doc['pros_person_image']
            filename2 = fs.save(pros_image.name,pros_image)
            pros_image_url = fs.url(filename2)
        else:
            pros_image_url = None

        try:
            case_model=Case(charge_id=charge_id,court_name=court_name,court_address=court_address,court_type=court_type,
            final_hearing=final_hearing,first_hearing=first_hearing,def_id=def_att_id,def_name=def_att_name,def_email=def_att_email,
            def_address=def_att_address,def_phone_no=def_att_phonenumber,def_DOB=def_att_DOB,pros_id=pros_att_id,pros_name=pros_att_name,
            pros_email=pros_att_email,pros_address=pros_att_address,pros_phone_no=pros_att_phonenumber,pros_DOB=pros_att_DOB,
            def_person_name=def_person_name,def_person_email=def_person_email,def_person_address=def_person_address,
            def_person_phone_no=def_person_phoneno,def_person_DOB=def_person_DOB,def_crime_type=def_person_crime,def_person_charges=def_person_charges,
            def_person_image=def_image_url,pros_person_name=pros_person_name,pros_person_email=pros_person_email,
            pros_person_address=pros_person_address,pros_person_phone_no=pros_person_phoneno,pros_person_DOB=pros_person_DOB,
            pros_person_desc=pros_person_charges,pros_person_image=pros_image_url,judge_id=get_judge_id,
            judge_name=judge_name,judge_email=judge_email,judge_address=judge_address,judge_phone_no=judge_phonenumber,judge_DOB=judge_DOB)
            case_model.save()
            chargesheet.status="Completed"
            chargesheet.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/view_all_cases")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_case/" + charge_id)

def add_attorney(request):
    return render(request,"court_template/add_attorney.html")

def add_attorney_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        attorney_name=request.POST.get("attorney_name")
        attorney_email=request.POST.get("attorney_email")
        attorney_sex=request.POST.get("attorney_sex")
        attorney_address=request.POST.get("attorney_address")
        attorney_phone_no=request.POST.get("attorney_phone_no")
        attorney_DOB=request.POST.get("attorney_DOB")

        try:
            attorney_model=Attorney(name=attorney_name,email=attorney_email,address=attorney_address,phone_no=attorney_phone_no,
            Sex=attorney_sex,DOB=attorney_DOB)
            attorney_model.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_attorney")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_attorney")

def view_attorney(request):
    attorneys=Attorney.objects.all()
    return render(request,"court_template/view_attorney.html",{"attorneys":attorneys})

def add_judge(request):
    return render(request,"court_template/add_judge.html")

def add_judge_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        judge_name=request.POST.get("judge_name")
        judge_email=request.POST.get("judge_email")
        judge_sex=request.POST.get("judge_sex")
        judge_address=request.POST.get("judge_address")
        judge_phone_no=request.POST.get("judge_phone_no")
        judge_DOB=request.POST.get("judge_DOB")

        try:
            judge_model=Judge(name=judge_name,email=judge_email,address=judge_address,phone_no=judge_phone_no,
            Sex=judge_sex,DOB=judge_DOB)
            judge_model.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_judge")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_judge")

def view_judge(request):
    judges=Judge.objects.all()
    return render(request,"court_template/view_judge.html",{"judges":judges})

def view_all_cases(request):
    cases=Case.objects.all()[::-1]
    case_ids=[i.id for i in cases]
    decisions=Decision.objects.all().filter(case_id__in = case_ids)
    decision_ids=[j.case_id for j in decisions]
    return render(request,"court_template/view_all_cases.html",{"cases":cases,"decision_ids":decision_ids})

def view_case(request,case_id):
    case=Case.objects.get(id=case_id)
    return render(request,"court_template/view_case.html",{"case":case})

def edit_case(request,case_id):
    case=Case.objects.get(id=case_id)
    username=request.user.username
    address=request.user.court.address
    court_type=request.user.court.court_type
    attorneys=Attorney.objects.all()
    judges=Judge.objects.all()
    return render(request,"court_template/edit_case.html",{"case":case,"username":username,
    "address":address,"court_type":court_type,"attorneys":attorneys,"judges":judges})

def edit_case_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        case_id=request.POST.get("case_id")
        court_name=request.POST.get("court_name")
        court_address=request.POST.get("court_address")
        court_type=request.POST.get("court_type")
        first_hearing=request.POST.get("first_hearing")
        final_hearing=request.POST.get("final_hearing")

        def_att_id=request.POST.get("def_att_id")
        def_att_name=request.POST.get("def_att_name")
        def_att_email=request.POST.get("def_att_email")
        def_att_address=request.POST.get("def_att_address")
        def_att_phonenumber=request.POST.get("def_att_phonenumber")
        def_att_DOB=request.POST.get("def_att_DOB")

        pros_att_id=request.POST.get("pros_att_id")
        pros_att_name=request.POST.get("pros_att_name")
        pros_att_email=request.POST.get("pros_att_email")
        pros_att_address=request.POST.get("pros_att_address")
        pros_att_phonenumber=request.POST.get("pros_att_phonenumber")
        pros_att_DOB=request.POST.get("pros_att_DOB")

        get_judge_id=request.POST.get("get_judge_id")
        judge_name=request.POST.get("judge_name")
        judge_email=request.POST.get("judge_email")
        judge_address=request.POST.get("judge_address")
        judge_phonenumber=request.POST.get("judge_phonenumber")
        judge_DOB=request.POST.get("judge_DOB")

        def_person_name=request.POST.get("def_person_name")
        def_person_email=request.POST.get("def_person_email")
        def_person_address=request.POST.get("def_person_address")
        def_person_phoneno=request.POST.get("def_person_phoneno")
        def_person_DOB=request.POST.get("def_person_DOB")
        def_person_charges=request.POST.get("def_person_charges")
        def_person_crime=request.POST.get("def_person_crime")
        
        pros_person_name=request.POST.get("pros_person_name")
        pros_person_email=request.POST.get("pros_person_email")
        pros_person_address=request.POST.get("pros_person_address")
        pros_person_phoneno=request.POST.get("pros_person_phoneno")
        pros_person_DOB=request.POST.get("pros_person_DOB")
        pros_person_charges=request.POST.get("pros_person_charges")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'def_person_image' in doc:
            def_image = doc['def_person_image']
            filename1 = fs.save(def_image.name,def_image)
            def_image_url = fs.url(filename1)
        else:
            def_image_url = None
        
        if 'pros_person_image' in doc:
            pros_image = doc['pros_person_image']
            filename2 = fs.save(pros_image.name,pros_image)
            pros_image_url = fs.url(filename2)
        else:
            pros_image_url = None

        try:
            case_model=Case.objects.get(id=int(case_id))

            case_model.court_name=court_name
            case_model.court_address=court_address
            case_model.court_type=court_type
            case_model.final_hearing=final_hearing
            case_model.first_hearing=first_hearing

            case_model.def_id=def_att_id
            case_model.def_name=def_att_name
            case_model.def_email=def_att_email
            case_model.def_address=def_att_address
            case_model.def_phone_no=def_att_phonenumber
            case_model.def_DOB=def_att_DOB
            
            case_model.pros_id=pros_att_id
            case_model.pros_name=pros_att_name
            case_model.pros_email=pros_att_email
            case_model.pros_address=pros_att_address
            case_model.pros_phone_no=pros_att_phonenumber
            case_model.pros_DOB=pros_att_DOB

            case_model.def_person_name=def_person_name
            case_model.def_person_email=def_person_email
            case_model.def_person_address=def_person_address
            case_model.def_person_phone_no=def_person_phoneno
            case_model.def_person_DOB=def_person_DOB
            case_model.def_crime_type=def_person_crime
            case_model.def_person_charges=def_person_charges
            if def_image_url != None:
                case_model.def_person_image=def_image_url
            
            case_model.pros_person_name=pros_person_name
            case_model.pros_person_email=pros_person_email
            case_model.pros_person_address=pros_person_address
            case_model.pros_person_phone_no=pros_person_phoneno
            case_model.pros_person_DOB=pros_person_DOB
            case_model.pros_person_desc=pros_person_charges
            if pros_image_url != None:
                case_model.pros_person_image=pros_image_url
            
            case_model.judge_id=get_judge_id
            case_model.judge_name=judge_name
            case_model.judge_email=judge_email
            case_model.judge_address=judge_address
            case_model.judge_phone_no=judge_phonenumber
            case_model.judge_DOB=judge_DOB

            case_model.save()

            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/view_case/"+case_id)
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_case/"+case_id)

def make_decision(request,case_id):
    case=Case.objects.get(id=case_id)
    return render(request,"court_template/make_decision.html",{"case":case})

def make_decision_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        case_id=request.POST.get("case_i")
        case_decision=request.POST.get("case_decision")
        decision_desc=request.POST.get("decision_desc")
        decision_reason=request.POST.get("decision_reason")

        if (case_decision != "") and (decision_desc != "") and (decision_reason != ""):
            decision_model=Decision(case_id=case_id,decision=case_decision,decision_reason=decision_reason,decision_desc=decision_desc)
            decision_model.save()
            decisions=Decision.objects.get(case_id=case_id)
            case=Case.objects.get(id=int(case_id))
            case.status="Completed"
            if case_decision == "Yes":
                return HttpResponseRedirect("/add_criminal/"+case_id)
            else:
                return HttpResponseRedirect("/add_release/"+case_id)
        else:
            messages.error(request,"All Fields are compulsory to fill")
            return HttpResponseRedirect("/make_decision/")

def add_criminal(request,case_id):
    decision=Decision.objects.get(case_id=case_id)
    jails=Jail.objects.all()
    return render(request,"court_template/add_criminal.html",{"decision":decision,"jails":jails})

def add_criminal_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        decision_id=request.POST.get("decision_i")
        case_id=request.POST.get("case_id")
        
        criminal_name=request.POST.get("criminal_name")
        criminal_email=request.POST.get("criminal_email")
        criminal_address=request.POST.get("criminal_address")
        criminal_phoneno=request.POST.get("criminal_phoneno")
        criminal_DOB=request.POST.get("criminal_DOB")
        criminal_sex=request.POST.get("criminal_sex")
        criminal_charges=request.POST.get("criminal_charges")
        criminal_sentence_sdate=request.POST.get("criminal_sentence_sdate")
        criminal_sentence_edate=request.POST.get("criminal_sentence_edate")

        crime_type=request.POST.get("crime_type")
        crime_name=request.POST.get("crime_name")
        crime_desc=request.POST.get("crime_desc")
        crime_date=request.POST.get("crime_date")
        crime_place=request.POST.get("crime_place")

        jail_id=request.POST.get("jail_id")
        jail_name=request.POST.get("jail_name")
        jail_email=request.POST.get("jail_email")
        jail_address=request.POST.get("jail_address")
        jail_jailer=request.POST.get("jail_jailer")
        jail_phoneno=request.POST.get("jail_phoneno")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'criminal_image' in doc:
            criminal_image = doc['criminal_image']
            filename1 = fs.save(criminal_image.name,criminal_image)
            criminal_image_url = fs.url(filename1)
        else:
            criminal_image_url = None
        
        try:
            criminal_model=Criminal(decision_id=decision_id,criminal_name=criminal_name,criminal_email=criminal_email,
            criminal_address=criminal_address,criminal_phone_no=criminal_phoneno,criminal_DOB=criminal_DOB,criminal_image=criminal_image_url,
            criminal_charges=criminal_charges,criminal_sentence_start=criminal_sentence_sdate,criminal_sentence_end=criminal_sentence_edate,
            crime_type=crime_type,crime_name=crime_name,crime_desc=crime_desc,crime_date=crime_date,crime_place=crime_place,
            jail_id=jail_id,jail_name=jail_name,jail_email=jail_email,jail_address=jail_address,jail_jailer=jail_jailer,jail_phoneno=jail_phoneno,
            status_health_record="Not_Uploaded",status_work="Not_Alloted",status="Sent",case_id=case_id)
            criminal_model.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/court_home")
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/add_criminal/"+str(decision_id))

def view_all_criminals(request):
    criminals=Criminal.objects.all()
    return render(request,"court_template/view_all_criminals.html",{"criminals":criminals})

def add_release(request,case_id):
    case=Case.objects.get(id=case_id)
    return render(request,"court_template/add_release.html",{"case":case})

def add_release_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        case_id=request.POST.get("case_i")

        release_type=request.POST.get("release_type")
        release_name=request.POST.get("release_name")
        release_email=request.POST.get("release_email")
        release_address=request.POST.get("release_address")
        release_phoneno=request.POST.get("release_phoneno")
        release_DOB=request.POST.get("release_DOB")
        release_sex=request.POST.get("release_sex")
        release_place=request.POST.get("release_place")
        release_date=request.POST.get("release_date")
        release_charges=request.POST.get("release_charges")
        
        fs=FileSystemStorage()
        doc=request.FILES

        if 'release_image' in doc:
            release_image = doc['release_image']
            filename1 = fs.save(release_image.name,release_image)
            release_image_url = fs.url(filename1)
        else:
            release_image_url = None
        
        try:
            release_model=Release(case_id=case_id,release_name=release_name,release_email=release_email,release_phone_no=release_phoneno,
            release_address=release_address,release_DOB=release_DOB,release_sex=release_sex,release_dropcharges=release_charges,
            release_time=release_date,release_place=release_place,release_type=release_type,release_image=release_image_url)
            release_model.save()
            return HttpResponseRedirect("/court_home")
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/add_release/"+str(case_id))

def view_all_releases(request):
    releases=Release.objects.all()
    return render(request,"court_template/view_all_releases.html",{"releases":releases})

@csrf_exempt
def get_def_att_info(request):
    def_id=request.POST.get("def_id")

    att=Attorney.objects.filter(id=int(def_id))    
    att_data=serializers.serialize('python',att)
    return JsonResponse(json.dumps(att_data,default=myconverter),content_type="application/json",safe=False)

@csrf_exempt
def get_judge_info(request):
    judge_id=request.POST.get("judge_id")

    judge=Judge.objects.filter(id=int(judge_id))    
    judge_data=serializers.serialize('python',judge)
    return JsonResponse(json.dumps(judge_data,default=myconverter),content_type="application/json",safe=False)

@csrf_exempt
def get_jail_info(request):
    jail_id=request.POST.get("jail_id")

    jail=Jail.objects.filter(id=jail_id)
    jail_data=serializers.serialize('python',jail)
    return JsonResponse(json.dumps(jail_data,default=myconverter),content_type="application/json",safe=False)
    
