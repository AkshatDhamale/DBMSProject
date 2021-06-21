from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import CustomUser,Criminal,Jail,Cell,Work,HealthRecord,Doctor,Meeting,Release,Decision
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime
import json

def myconverter(o):    
    return o.strftime('%Y-%m-%d')

def jail_home(request):
    criminals_notadded_count=Criminal.objects.all().filter(status="Sent").count()
    criminals_nowork_count=Criminal.objects.all().filter(status_work="Not_Alloted").count()
    criminals_nohealth_count=Criminal.objects.all().filter(status_health_record="Not_Uploaded").count()
    criminals=Criminal.objects.all()[::-1][:5]
    jails=Jail.objects.all()[:5]
    return render(request,"jail_template/base_template_jail.html",{"criminals_notadded_count":criminals_notadded_count,
    "criminals_nowork_count":criminals_nowork_count,"criminals_nohealth_count":criminals_nohealth_count,"criminals":criminals,
    "jails":jails})

def jail_account(request):
    jail=Jail.objects.get(admin_id=request.user.id)
    return render(request,"jail_template/jail_account.html",{"jail":jail})

def jail_account_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        jail_id=request.POST.get('jail_id')
        jail_address=request.POST.get('jail_address')
        jail_phone_number=request.POST.get('jail_phone_number')
        jail_jailer=request.POST.get('jail_jailer')

        try:
            jail_model=Jail.objects.get(id=jail_id)
            jail_model.address=jail_address
            jail_model.phonenumber=jail_phone_number
            jail_model.jailer=jail_jailer
            jail_model.save()
            messages.success(request,"Successfully edited")
            return HttpResponseRedirect("/jail_account")
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/jail_account")

def view_not_alloted(request):
    criminals=Criminal.objects.all().filter(status="Sent")
    return render(request,"jail_template/view_not_alloted.html",{'criminals':criminals})

def add_cell(request):
    jail=Jail.objects.get(jail_name=request.user.username)
    return render(request,"jail_template/add_cell.html",{'jail':jail})

def add_cell_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        jail_id=request.POST.get("jail_i")
        cell_type=request.POST.get("cell_type")
        cell_section=request.POST.get("cell_section")
        cell_number=request.POST.get("cell_number")

        try:
            cell_model=Cell(jail_id=jail_id,cell_type=cell_type,cell_section=cell_section,cell_number=cell_number)
            cell_model.save()
            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/add_cell")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/add_cell")

def view_all_cell(request):
    cells=Cell.objects.all()    
    return render(request,"jail_template/view_all_cell.html",{'cells':cells})

def edit_cell(request,cell_id):
    cell=Cell.objects.get(id=cell_id)
    jail=Jail.objects.get(jail_name=request.user.username)
    criminals=Criminal.objects.all()
    return render(request,"jail_template/edit_cell.html",{'cell':cell,'jail':jail,'criminals':criminals})

def edit_cell_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        cell_id=request.POST.get("cell_id")
        criminal_id=request.POST.get("criminal_id")
        jail_id=request.POST.get("jail_i")
        cell_type=request.POST.get("cell_type")
        cell_section=request.POST.get("cell_section")
        cell_number=request.POST.get("cell_number")

        try:
            cell_model=Cell.objects.get(id=cell_id)

            cell_model.criminal_id=criminal_id
            cell_model.cell_type=cell_type
            cell_model.cell_section=cell_section
            cell_model.cell_number=cell_number
            cell_model.save()            
            return HttpResponseRedirect("/view_all_cell")
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_cell/"+str(cell_id))

def remove_cell(request,cell_id):
    cell=Cell.objects.get(id=cell_id)

    try:
        cell.delete()
        messages.success(request,"Successfully deleted the cell")
        return HttpResponseRedirect("/view_all_cell")
    except:
        messages.error(request,"Failed to delete the cell")
        return HttpResponseRedirect("/view_all_cell")

def view_all_criminal(request):
    criminals=Criminal.objects.all()
    cells=Cell.objects.all()
    counts=[]
    for i in criminals:
        count = 0
        for j in cells:
            if j.criminal_id == i.id:
                count = j.id
                break
        counts.append(count)
    countdict=zip(criminals,counts)
    return render(request,"jail_template/view_all_criminal.html",{"countdict":countdict})

def view_criminal_details(request,criminal_id):
    criminal=Criminal.objects.get(id=criminal_id)
    try:
        cell = Cell.objects.get(criminal_id=criminal_id)
    except Cell.DoesNotExist:
        cell = None
    return render(request,"jail_template/view_criminal_details.html",{"criminal":criminal,"cell":cell})

def allot_cell(request,criminal_id):
    criminal=Criminal.objects.get(id=criminal_id)
    jail=Jail.objects.get(id=criminal.jail_id)
    cells=Cell.objects.all()
    return render(request,"jail_template/allot_cell.html",{"criminal":criminal,"jail":jail,"cells":cells})

def allot_cell_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        cell_id=request.POST.get("cell_id")
        criminal_id=request.POST.get("criminal_id")

        try:
            cell_model=Cell.objects.get(id=int(cell_id))
            criminal_model=Criminal.objects.get(id=int(criminal_id))
            criminal_model.status="Added"            
            cell_model.criminal_id=criminal_id 
            criminal_model.save()
            cell_model.save()                                  
            return HttpResponseRedirect("/view_all_cell")
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/allot_cell/"+str(criminal_id))

def view_alloted(request):
    criminals=Criminal.objects.all().filter(status="Added")
    return render(request,"jail_template/view_alloted.html",{"criminals":criminals})

def release_criminal(request,criminal_id):
    criminal=Criminal.objects.get(id=criminal_id)
    jail=Jail.objects.get(id=criminal.jail_id)
    return render(request,"jail_template/release_criminal.html",{"criminal":criminal,"jail":jail})

def release_criminal_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        criminal_id=request.POST.get("criminal_id")
        release_date=request.POST.get("release_date")
        release_time=request.POST.get("release_time")
        release_place=request.POST.get("release_place")

        try:
            criminal=Criminal.objects.get(id=criminal_id)
            decision=Decision.objects.get(criminal_id=criminal_id)

            release_model=Release(case_id=decision.case_id,release_name=criminal.criminal_name,release_email=criminal.criminal_email,
            release_phone_no=criminal.criminal_phone_no,release_address=criminal.criminal_address,
            release_DOB=criminal.criminal_DOB,release_sex=criminal.criminal_sex,release_dropcharges=criminal.criminal_charges,
            release_date=release_date,release_time=release_time,release_place=release_place,release_type="Convicted",
            release_image=criminal.criminal_image)   
            release_model.save()

            criminal.status="Released"

            messages.success(request,"Successfully Released the Criminal")                              
            return HttpResponseRedirect("/view_alloted")
        except:
            messages.error(request,"Failed to Release")
            return HttpResponseRedirect("/view_alloted")
    
def assign_work(request):
    criminals=Criminal.objects.all().filter(status_work="Not_Alloted")
    return render(request,"jail_template/assign_work.html",{"criminals":criminals})

def assign_work_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        criminal_id=request.POST.get("criminal_id")
        jail_id=request.POST.get("jail_id")

        work_type=request.POST.get("work_type")
        work_name=request.POST.get("work_name")
        work_desc=request.POST.get("work_desc")
        work_duration=request.POST.get("work_duration")
        work_start_time=request.POST.get("work_start_time")
        work_end_time=request.POST.get("work_end_time")

        try:
            work_model=Work(criminal_id=criminal_id,jail_id=jail_id,work_type=work_type,work_name=work_name,work_desc=work_desc,
            work_duration=work_duration,work_start_time=work_start_time,work_end_time=work_end_time) 
            work_model.save()
            criminal=Criminal.objects.get(id=criminal_id)
            criminal.status_work='Alloted'
            criminal.save()
            messages.success(request,"Successfully alloted the cell")                              
            return HttpResponseRedirect("/assign_work")
        except:
            messages.error(request,"Failed to allot")
            return HttpResponseRedirect("/assign_work")

def view_all_work(request):
    works=Work.objects.all()
    return render(request,"jail_template/view_all_work.html",{"works":works})

def view_healthrecord(request):
    healthrecord=HealthRecord.objects.all()
    criminals=Criminal.objects.all().filter(status_health_record='Uploaded')
    return render(request,"jail_template/view_healthrecord.html",{"healthrecord":healthrecord,"criminals":criminals})

def view_new_meeting(request):
    meetings=Meeting.objects.all().filter(status="Pending")
    return render(request,"jail_template/view_new_meeting.html",{"meetings":meetings})

def view_meeting_details(request,meeting_id):
    meeting=Meeting.objects.get(id=meeting_id)
    criminal=Criminal.objects.get(id=meeting.criminal_id)
    return render(request,"jail_template/view_meeting_details.html",{"meeting":meeting,"criminal":criminal})

def meeting_grant(request,meeting_id):
    meeting=Meeting.objects.get(id=meeting_id)
    criminal=Criminal.objects.get(id=meeting.criminal_id)
    return render(request,"jail_template/meeting_grant.html",{"meeting":meeting,"criminal":criminal})

def view_past_meetings(request):
    meetings=Meeting.objects.all().filter(Q(status="Granted") | Q(status="Denied"))
    return render(request,"jail_template/view_past_meetings.html",{"meetings":meetings})

def grant_meeting_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        meeting_id=request.POST.get("meeting_id")
        meeting_actual_date=request.POST.get("meeting_actual_date")
        meeting_start_time=request.POST.get("meeting_start_time")
        meeting_end_time=request.POST.get("meeting_end_time")
        meeting_room=request.POST.get("meeting_room")        

        try:
            meeting_model=Meeting.objects.get(id=meeting_id)

            meeting_model.meeting_actual_date=meeting_actual_date
            meeting_model.meeting_start_time=meeting_start_time
            meeting_model.meeting_end_time=meeting_end_time
            meeting_model.meeting_room=meeting_room
            meeting_model.status='Granted'

            meeting_model.save()            
            messages.success(request,"Successfully Granted the meeting permission")                              
            return HttpResponseRedirect("/meeting_grant/"+str(meeting_id))
        except:
            messages.error(request,"Failed to Grant")
            return HttpResponseRedirect("/meeting_grant/"+str(meeting_id))

def view_released(request):
    releases=Release.objects.all().filter(release_type="Convicted")
    return render(request,"jail_template/view_released.html",{"releases":releases})

def meeting_reject(request,meeting_id):
    meeting=Meeting.objects.get(id=meeting_id)
    criminal=Criminal.objects.get(id=meeting.criminal_id)
    return render(request,"jail_template/meeting_reject.html",{"meeting":meeting,"criminal":criminal})

def reject_meeting_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        meeting_id=request.POST.get("meeting_id")
        meeting_reason=request.POST.get("meeting_reason")

        try:
            meeting_model=Meeting.objects.get(id=meeting_id)
            meeting_model.reject_reason=meeting_reason
            meeting_model.status="Denied"
            meeting_model.save()   
            messages.success(request,"Successfully Denied the meeting permission")                              
            return HttpResponseRedirect("/meeting_reject/"+str(meeting_id))
        except:
            messages.error(request,"Failed to Deny")
            return HttpResponseRedirect("/meeting_reject/"+str(meeting_id))

def view_past_meeting_details(request,meeting_id):
    meeting=Meeting.objects.get(id=meeting_id)
    criminal=Criminal.objects.get(id=meeting.criminal_id)
    return render(request,"jail_template/view_past_meeting_details.html",{"meeting":meeting,"criminal":criminal})

@csrf_exempt
def get_all_info(request):
    criminal_id=request.POST.get("criminal_id")

    criminal=Criminal.objects.get(id=int(criminal_id))
    healthrecord=HealthRecord.objects.get(criminal_id=int(criminal_id))
    doctor_id=healthrecord.doctor_id
    doctor=Doctor.objects.get(id=doctor_id)   
    list_data=[{"criminal_name":criminal.criminal_name,"jail_id":criminal.jail_id,"criminal_DOB":criminal.criminal_DOB,
    "criminal_image":criminal.criminal_image.url[6:],"criminal_sentence_duration":criminal.criminal_sentence_duration,"criminal_sex":criminal.criminal_sex},
    {"doctor_id":doctor.id,"doctor_name":doctor.admin.username,"doctor_email":doctor.admin.email,"doctor_address":doctor.address,
    "doctor_phonenumber":doctor.phonenumber},
    {"previous_diseases":healthrecord.previous_diseases,"family_diseases":healthrecord.family_diseases,"allergies":healthrecord.allergies,
    "current_diseases":healthrecord.current_diseases,"current_medications":healthrecord.current_medications,"height":healthrecord.height,
    "weight":healthrecord.weight,"BMI":healthrecord.BMI,"BP":healthrecord.BP,"Hearing":healthrecord.Hearing,"Vision":healthrecord.Vision,"Dental":healthrecord.Dental,
    "x_ray_results":healthrecord.x_ray_results,"abornmalities":healthrecord.abornmalities,"mental_report":healthrecord.mental_report,
    "x_ray_report":healthrecord.x_ray_report.url[6:],"signature":healthrecord.signature.url[6:]}]

    return JsonResponse(json.dumps(list_data,default=myconverter),content_type="application/json",safe=False)

@csrf_exempt
def get_cell_info(request):
    cell_id=request.POST.get("cell_id")

    cell=Cell.objects.filter(id=int(cell_id))    
    cell_data=serializers.serialize('python',cell)
    return JsonResponse(json.dumps(cell_data,default=myconverter),content_type="application/json",safe=False)

@csrf_exempt
def get_criminal_info(request):
    criminal_id=request.POST.get("criminal_id")

    criminal=Criminal.objects.filter(id=int(criminal_id))    
    criminal_data=serializers.serialize('python',criminal)
    return JsonResponse(json.dumps(criminal_data,default=myconverter),content_type="application/json",safe=False)

