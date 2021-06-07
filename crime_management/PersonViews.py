from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import CustomUser,RegisterPerson,Report,Criminal,Meeting,Jail
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.utils.timezone import now
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

def myconverter(o):    
    return o.strftime('%Y-%m-%d')

def person_home(request):
    return render(request,"person_template/base_template_person.html")

def report_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_by_type=request.POST.get("report_by_type")
        person_id=request.POST.get("person_id")
        inf_name=request.POST.get("inf_name")
        inf_email=request.POST.get("inf_email")
        inf_sex=request.POST.get("inf_sex")
        inf_address=request.POST.get("inf_address")
        inf_phonenumber=request.POST.get("inf_phonenumber")

        report_against_type=request.POST.get("report_against_type")
        report_against_name=request.POST.get("report_against_name")
        report_against_email=request.POST.get("report_against_email")
        report_against_sex=request.POST.get("report_against_sex")
        report_against_address=request.POST.get("report_against_address")
        report_against_phonenumber=request.POST.get("report_against_phonenumber")

        event_date=request.POST.get("event_date")
        event_type=request.POST.get("event_type")
        event_address=request.POST.get("event_address")
        event_description=request.POST.get("event_description")        

        fs=FileSystemStorage()
        doc=request.FILES

        if 'report_against_image' in doc:
            report_against_image=doc['report_against_image']
            filename=fs.save(report_against_image.name,report_against_image)
            report_against_image_url=fs.url(filename)
        else:
            report_against_image_url=None

        if 'inf_image' in doc:
            report_by_image=doc['inf_image']
            filename2=fs.save(report_by_image.name,report_by_image)
            report_by_image_url=fs.url(filename2)
        else:
            report_by_image_url=None

        try:
            Report_model=Report(reportagainst=report_against_type,person_id=int(person_id),reportagainst_name=report_against_name,reportagainst_email=report_against_email,
            reportagainst_address=report_against_address,reportagainst_phonenumber=report_against_phonenumber,reportagainstsex=report_against_sex,
            eventdate=event_date,eventtype=event_type,eventaddress=event_address,eventdescription=event_description,
            report_by_type=report_by_type,inf_name=inf_name,inf_email=inf_email,inf_sex=inf_sex,inf_address=inf_address,
            inf_phonenumber=inf_phonenumber,reportagainst_image=report_against_image_url,inf_image=report_by_image_url)

            Report_model.save()
            messages.success(request,"Successfully filed the report")
            return HttpResponseRedirect("/person_home")
        except:
            messages.error(request,"Failed to file the report")
            return HttpResponseRedirect("/person_home")

def arrange_meeting(request):
    criminals=Criminal.objects.all()
    return render(request,"person_template/arrange_meeting.html",{"criminals":criminals})

def arrange_meeting_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:      
        person_id=request.POST.get("person_id")  
        meeting_name=request.POST.get("meeting_name")
        meeting_email=request.POST.get("meeting_email")
        meeting_DOB=request.POST.get("meeting_DOB")
        meeting_sex=request.POST.get("meeting_sex")
        meeting_address=request.POST.get("meeting_address")
        meeting_phonenumber=request.POST.get("meeting_phonenumber")

        occupation_type=request.POST.get("occupation_type")
        occupation_name=request.POST.get("occupation_name")
        occupation_address=request.POST.get("occupation_address")
        occupation_phonenumber=request.POST.get("occupation_phonenumber")

        criminal_name=request.POST.get("criminal_name")
        criminal_id=request.POST.get("criminal_id")
        jail_id=request.POST.get("jail_id")
        criminal_relation=request.POST.get("criminal_relation")
        criminal_reason=request.POST.get("criminal_reason")
        meeting_preferred_date=request.POST.get("meeting_preferred_date")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'meeting_image' in doc:
            meeting_image = doc['meeting_image']
            filename1 = fs.save(meeting_image.name,meeting_image)
            meeting_image_url = fs.url(filename1)
        else:
            meeting_image_url = None

        try:
            meeting_model=Meeting(person_id=person_id,meeting_name=meeting_name,meeting_address=meeting_address,meeting_email=meeting_email,meeting_DOB=meeting_DOB,
            meeting_sex=meeting_sex,meeting_phonenumber=meeting_phonenumber,meeting_image=meeting_image_url,
            occupation_type=occupation_type,occupation_name=occupation_name,occupation_address=occupation_address,
            occupation_phonenumber=occupation_phonenumber,criminal_name=criminal_name,criminal_id=criminal_id,jail_id=jail_id,
            meeting_date=meeting_preferred_date,criminal_relation=criminal_relation,criminal_reason=criminal_reason)
            meeting_model.save()
            messages.success(request,"Successfully sent the request")
            return HttpResponseRedirect("/arrange_meeting")
        except:
            messages.error(request,"Failed to send the request")
            return HttpResponseRedirect("/arrange_meeting")

def view_previous_reports(request):
    user_id = request.user.id
    reports=Report.objects.all().filter(person_id=user_id)
    return render(request,"person_template/view_previous_reports.html",{"reports":reports})

def view_report(request,report_id):
    report=Report.objects.get(id=report_id)
    return render(request,"person_template/view_report.html",{"report":report})

def view_all_meetings(request):
    user_id = request.user.id
    meetings=Meeting.objects.all().filter(person_id=user_id)
    Jails=Jail.objects.all()
    counts=[]
    for i in meetings:
        count = ''
        for j in Jails:
            if i.jail_id == j.id:
                count += j.admin.username
        counts.append(count)
    countdict=zip(meetings,counts)
    return render(request,"person_template/view_all_meetings.html",{"countdict":countdict})

def view_meet_details(request,meeting_id):
    meeting=Meeting.objects.get(id=meeting_id)
    return render(request,"person_template/view_meeting.html",{"meeting":meeting})


@csrf_exempt
def get_criminal_meeting(request):
    criminal_name=request.POST.get("criminal_name")

    criminal=Criminal.objects.filter(criminal_name=criminal_name)    
    criminal_data=serializers.serialize('python',criminal)
    return JsonResponse(json.dumps(criminal_data,default=myconverter),content_type="application/json",safe=False)

