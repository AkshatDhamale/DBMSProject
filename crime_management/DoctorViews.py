from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import CustomUser,Doctor,Criminal,HealthRecord
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

def myconverter(o):    
    return o.strftime('%Y-%m-%d')

def doctor_home(request):
    return render(request,"doctor_template/base_template_doctor.html")

def add_health_record(request):
    username=request.user.username
    email=request.user.email
    doc_id=request.user.id
    doctor=Doctor.objects.get(admin_id=doc_id)
    criminals=Criminal.objects.all()
    return render(request,"doctor_template/add_health_record.html",{"doctor":doctor,"username":username,"email":email,"criminals":criminals})

def add_health_record_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        criminal_id=request.POST.get("criminal_id")
        doctor_id=request.POST.get("doctor_i")
        jail_id=request.POST.get("jail_id")
        criminal_name=request.POST.get("criminal_name")

        previous_diseases=request.POST.get("previous_diseases")
        family_diseases=request.POST.get("family_diseases")
        allergies=request.POST.get("allergies")
        current_diseases=request.POST.get("current_diseases")
        current_medications=request.POST.get("current_medications")

        height=request.POST.get("height")
        weight=request.POST.get("weight")
        BMI=request.POST.get("BMI")
        BP=request.POST.get("BP")
        Hearing=request.POST.get("Hearing")
        Vision=request.POST.get("Vision")
        Dental=request.POST.get("Dental")

        x_ray_results=request.POST.get("x_ray_results")
        abornmalities=request.POST.get("abornmalities")
        mental_report=request.POST.get("mental_report")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'x_ray_report' in doc:
            x_ray_report = doc['x_ray_report']
            filename1 = fs.save(x_ray_report.name,x_ray_report)
            x_ray_report_url = fs.url(filename1)
        else:
            Accused_image_url = None
        
        if 'signature' in doc:
            signature = doc['signature']
            filename2 = fs.save(signature.name,signature)
            signature_url = fs.url(filename2)
        else:
            signature_url = None

        try:
            healthrecord_model=HealthRecord(criminal_id=criminal_id,jail_id=jail_id,criminal_name=criminal_name,doctor_id=doctor_id,previous_diseases=previous_diseases,family_diseases=family_diseases,
            allergies=allergies,current_diseases=current_diseases,current_medications=current_medications,height=height,weight=weight,
            BMI=BMI,BP=BP,Hearing=Hearing,Vision=Vision,Dental=Dental,x_ray_results=x_ray_results,abornmalities=abornmalities,
            mental_report=mental_report,x_ray_report=x_ray_report_url,signature=signature_url)
            healthrecord_model.save()
            criminal_model=Criminal.objects.get(id=criminal_id)
            criminal_model.status_health_record='Uploaded' 
            criminal_model.save()           
            messages.success(request,"Successfully made Health Record")                              
            return HttpResponseRedirect("/add_health_record")
        except:
            messages.error(request,"Failed to make")
            return HttpResponseRedirect("/add_health_record")

def view_all_health_record(request):
    healthrecords=HealthRecord.objects.all()
    return render(request,"doctor_template/view_all_health_record.html",{"healthrecords":healthrecords})

def edit_health_record(request,healthrecord_id):
    healthrecord=HealthRecord.objects.get(id=healthrecord_id)
    doc_id=request.user.id
    doctor=Doctor.objects.get(admin_id=doc_id)
    criminals=Criminal.objects.all()
    return render(request,"doctor_template/edit_health_record.html",{"healthrecord":healthrecord,"doctor":doctor,"criminals":criminals})

def edit_health_record_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        healthrecord_id=request.POST.get("healthrecord_id")
        criminal_id=request.POST.get("criminal_id")
        doctor_id=request.POST.get("doctor_i")
        jail_id=request.POST.get("jail_id")
        criminal_name=request.POST.get("criminal_name")

        previous_diseases=request.POST.get("previous_diseases")
        family_diseases=request.POST.get("family_diseases")
        allergies=request.POST.get("allergies")
        current_diseases=request.POST.get("current_diseases")
        current_medications=request.POST.get("current_medications")

        height=request.POST.get("height")
        weight=request.POST.get("weight")
        BMI=request.POST.get("BMI")
        BP=request.POST.get("BP")
        Hearing=request.POST.get("Hearing")
        Vision=request.POST.get("Vision")
        Dental=request.POST.get("Dental")

        x_ray_results=request.POST.get("x_ray_results")
        abornmalities=request.POST.get("abornmalities")
        mental_report=request.POST.get("mental_report")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'x_ray_report' in doc:
            x_ray_report = doc['x_ray_report']
            filename1 = fs.save(x_ray_report.name,x_ray_report)
            x_ray_report_url = fs.url(filename1)
        else:
            Accused_image_url = None
        
        if 'signature' in doc:
            signature = doc['signature']
            filename2 = fs.save(signature.name,signature)
            signature_url = fs.url(filename2)
        else:
            signature_url = None

        try:
            healthrecord_model=HealthRecord.objects.get(id=healthrecord_id) 

            healthrecord_model.criminal_id=criminal_id
            healthrecord_model.doctor_id=doctor_id
            healthrecord_model.jail_id=jail_id
            healthrecord_model.criminal_name=criminal_name

            healthrecord_model.previous_diseases=previous_diseases
            healthrecord_model.family_diseases=family_diseases
            healthrecord_model.allergies=allergies
            healthrecord_model.current_diseases=current_diseases
            healthrecord_model.current_medications=current_medications
            
            healthrecord_model.height=height
            healthrecord_model.weight=weight
            healthrecord_model.BMI=BMI
            healthrecord_model.BP=BP
            healthrecord_model.Hearing=Hearing
            healthrecord_model.Vision=Vision
            healthrecord_model.Dental=Dental

            healthrecord_model.x_ray_results=x_ray_results
            healthrecord_model.abornmalities=abornmalities
            healthrecord_model.mental_report=mental_report

            if healthrecord_model.x_ray_report != None:
                healthrecord_model.x_ray_report=x_ray_report_url

            if healthrecord_model.signature != None:
                healthrecord_model.signature=signature_url

            healthrecord_model.save()         
            messages.success(request,"Successfully edited the Health Record")                              
            return HttpResponseRedirect("/edit_health_record/"+str(healthrecord_id))
        except:
            messages.error(request,"Failed to edit")
            return HttpResponseRedirect("/edit_health_record/"+str(healthrecord_id))


@csrf_exempt
def doc_criminal_info(request):
    criminal_id=request.POST.get("criminal_id")

    criminal=Criminal.objects.filter(id=int(criminal_id))    
    criminal_data=serializers.serialize('python',criminal)
    return JsonResponse(json.dumps(criminal_data,default=myconverter),content_type="application/json",safe=False)

