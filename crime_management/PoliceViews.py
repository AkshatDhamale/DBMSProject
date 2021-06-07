from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
from crime_management.models import CustomUser,ChargeSheet,Report,Witnesses,Suspects,Theories,Police,Investigation_Report,Criminal,Cell
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import datetime
import json

def myconverter(o):    
    return o.strftime('%Y-%m-%d')

def police_home(request):
    reps=Report.objects.all().filter(status="Pending")[::-1]
    num_reports=len(reps)
    police=Police.objects.get(admin_id=request.user.id)
    return render(request,"police_template/base_template.html",{"reps":reps,"num_reports":num_reports,"police":police})

def view_charge_sheets(request):
    reports=Report.objects.all().filter(status="Viewed")
    reportids=[i.id for i in reports]
    investigations=Investigation_Report.objects.all().filter(report_id__in = reportids)
    return render(request,"police_template/view_charge_sheets.html",{"investigations":investigations})

def Charge_sheet(request,rep_id):
    username=request.user.username
    report=Report.objects.get(id=rep_id)
    return render(request,"police_template/Charge_Sheet.html",{"username":username,"report":report})

def Charge_sheet_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")

        charging_officer=request.POST.get("charging_officer")
        Accused_name=request.POST.get("Accused_name")
        Accused_address=request.POST.get("Accused_address")
        Accused_phonenumber=request.POST.get("Accused_phonenumber")
        Accused_email=request.POST.get("Accused_email")
        Accused_DOB=request.POST.get("Accused_DOB")
        Accused_sex=request.POST.get("Accused_sex")
        Accused_Charges=request.POST.get("Accused_Charges")
        Accused_law=request.POST.get("Accused_law")
        Accused_offense=request.POST.get("Accused_offense")
        Accused_act=request.POST.get("Accused_act")
        Accused_section=request.POST.get("Accused_section")

        Informant_name=request.POST.get("Informant_name")
        Informant_sex=request.POST.get("Informant_sex")
        Informant_DOB=request.POST.get("Informant_DOB")
        Informant_address=request.POST.get("Informant_address")
        Informant_Phonenumber=request.POST.get("Informant_Phonenumber")
        Informant_description=request.POST.get("Informant_description")
        Initial_report=request.POST.get("Initial_report")

        Reporting_officer=request.POST.get("Reporting_officer")
        Investigation_officer=request.POST.get("Investigation_officer")
        Assisting_officer=request.POST.get("Assisting_officer")
        Issued_at=request.POST.get("Issued_at")
        Issued_when=request.POST.get("Issued_when")
        Investigation_details=request.POST.get("Investigation_details")
        Theories=request.POST.get("Theories")
        Witnesses=request.POST.get("Witnesses")
        Suspects=request.POST.get("Suspects")

        Theory_1=request.POST.get("Theory_1")
        Theory_2=request.POST.get("Theory_2")
        Theory_3=request.POST.get("Theory_3")
        Theory_4=request.POST.get("Theory_4")
        Theory_5=request.POST.get("Theory_5")

        Witness_1=request.POST.get("Witness_1")
        Witness_2=request.POST.get("Witness_2")
        Witness_3=request.POST.get("Witness_3")
        Witness_4=request.POST.get("Witness_4")
        Witness_5=request.POST.get("Witness_5")

        Suspect_1=request.POST.get("Suspect_1")
        Suspect_2=request.POST.get("Suspect_2")
        Suspect_3=request.POST.get("Suspect_3")
        Suspect_4=request.POST.get("Suspect_4")
        Suspect_5=request.POST.get("Suspect_5")

        fs=FileSystemStorage()
        doc=request.FILES

        if 'Accused_image' in doc:
            Accused_image = doc['Accused_image']
            filename1 = fs.save(Accused_image.name,Accused_image)
            Accused_image_url = fs.url(filename1)
        else:
            Accused_image_url = None
        
        if 'Informant_image' in doc:
            Informant_image = doc['Informant_image']
            filename2 = fs.save(Informant_image.name,Informant_image)
            Informant_image_url = fs.url(filename2)
        else:
            Informant_image_url = None

        if 'Informant_signature' in doc:
            Informant_signature = doc['Informant_signature']
            filename3 = fs.save(Informant_signature.name,Informant_signature)
            Informant_signature_url = fs.url(filename3)
        else:
            Informant_signature_url = None

        try:
            Charge_sheet_model=ChargeSheet(report_id=report_id,Accused_name=Accused_name,Accused_address=Accused_address,charging_officer=charging_officer,
            Accused_phone_no=Accused_phonenumber,Accused_email=Accused_email,Accused_sex=Accused_sex,Accused_Charges=Accused_Charges,
            Accused_DOB=Accused_DOB,Accused_underwhatlaw=Accused_law,Accused_typeofoffense=Accused_offense,Accused_Act=Accused_act,
            Accused_section=Accused_section,Accused_image=Accused_image_url,
            Informant_name=Informant_name,Informant_address=Informant_address,Informant_phone_no=Informant_Phonenumber,
            Informant_description=Informant_description,Informant_DOB=Informant_DOB,Informant_sex=Informant_sex,
            Informant_initial_report=Initial_report,Informant_image=Informant_image_url,Informant_signature=Informant_signature_url,
            Reporting_officer=Reporting_officer,Investigation_officer=Investigation_officer,Assisting_officer=Assisting_officer,
            Issued_at=Issued_at,Issued_when=Issued_when,Investigation_details=Investigation_details,Theories=Theories,
            Witnesses=Witnesses,Suspects=Suspects,Theory1=Theory_1,Theory2=Theory_2,Theory3=Theory_3,Theory4=Theory_4,Theory5=Theory_5,
            Witness1=Witness_1,Witness2=Witness_2,Witness3=Witness_3,Witness4=Witness_4,Witness5=Witness_5,
            Suspect1=Suspect_1,Suspect2=Suspect_2,Suspect3=Suspect_3,Suspect4=Suspect_4,Suspect5=Suspect_5)
            Charge_sheet_model.save()

            report_model=Report.objects.get(id=report_id)
            report_model.status="Filed"
            report_model.save()

            messages.success(request,"Successfully added")
            return HttpResponseRedirect("/view_charge_sheets")
        except:
            messages.error(request,"Failed to add")
            return HttpResponseRedirect("/view_charge_sheets")

def view_report_all(request):
    report=Report.objects.all()
    return render(request,"police_template/view_report_all.html",{"report":report})

def edit_report(request,rep_id):
    report=Report.objects.get(id=rep_id)
    return render(request,"police_template/edit_report.html",{"report":report})

def edit_report_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not allowed</h2>")
    else:
        report_id=request.POST.get("report_id")
        report_by_type=request.POST.get("report_by_type")
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
        report_status=request.POST.get("report_status")

        try:
            report_model=Report.objects.get(id=int(report_id))

            report_model.report_by_type=report_by_type
            report_model.inf_name=inf_name
            report_model.inf_email=inf_email
            report_model.inf_sex=inf_sex
            report_model.inf_address=inf_address
            report_model.inf_phonenumber=inf_phonenumber

            report_model.reportagainst=report_against_type
            report_model.reportagainst_name=report_against_name
            report_model.reportagainst_email=report_against_email
            report_model.reportagainstsex=report_against_sex
            report_model.reportagainst_address=report_against_address
            report_model.reportagainst_phonenumber=report_against_phonenumber

            report_model.eventdate=event_date
            report_model.eventtype=event_type
            report_model.eventaddress=event_address
            report_model.eventdescription=event_description
            report_model.status=report_status
            
            report_model.save()
            messages.success(request,"Successfully edited the report")
            return HttpResponseRedirect("/edit_report/"+report_id)
        except:
            messages.error(request,"Failed to edit the report")
            return HttpResponseRedirect("/edit_report/"+report_id)

def view_completed_report(request):
    reports=Report.objects.all().filter(status="Filed")
    return render(request,"police_template/view_completed_report.html",{"reports":reports})

def view_dismissed_report(request):
    reports=Report.objects.all().filter(status="Dismissed")
    return render(request,"police_template/view_dismissed_report.html",{"reports":reports})

def view_witnesses(request):
    reports=Report.objects.all()
    witness=Witnesses.objects.all()
    counts=[]
    for i in reports:
        count = 0
        for j in witness:
            if i.id == j.report_id:
                count += 1
        counts.append(count)
    countdict=zip(reports,counts)
    return render(request,"police_template/view_witnesses.html",{"reports":reports,"countdict":countdict})

def add_witness(request,rep_id):
    report=Report.objects.get(id=rep_id)
    return render(request,"police_template/add_witness.html",{"report":report})

def add_witness_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        n=int(request.POST.get("number_witness"))
        for i in range(1,n+1):
            witness_name=request.POST.get("Witness_"+str(i)+"_name")
            witness_email=request.POST.get("Witness_"+str(i)+"_email")
            witness_address=request.POST.get("Witness_"+str(i)+"_address")
            witness_phonenumber=request.POST.get("Witness_"+str(i)+"_phonenumber")
            witness_DOB=request.POST.get("Witness_"+str(i)+"_DOB")
            witness_description=request.POST.get("Witness_"+str(i)+"_description")

            try:
                witness_model=Witnesses(report_id=report_id,name=witness_name,email=witness_email,address=witness_address,
                phone_no=witness_phonenumber,description=witness_description,DOB=witness_DOB)
                witness_model.save()
            except:
                messages.error(request,"Failed to add the witnesses")
                return HttpResponseRedirect("/add_witness/"+report_id)
    
        return HttpResponseRedirect("/view_witnesses")            

def remove_witness(request,rep_id):
    report=Report.objects.get(id=rep_id)
    witnesses=Witnesses.objects.all().filter(report_id=report.id)
    return render(request,"police_template/remove_witness.html",{"report":report,"witnesses":witnesses})

def remove_witness_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        witness_number=request.POST.get("select_witness")
        witness=Witnesses.objects.get(id=witness_number)
        
        try:
            witness.delete()
            messages.success(request,"Successfully deleted the Witness")
            return HttpResponseRedirect("/remove_witness/"+report_id)
        except:
            messages.error(request,"Failed to delete the witness")
            return HttpResponseRedirect("/remove_witness/"+report_id)
    
def show_witness(request,rep_id):
    report=Report.objects.get(id=rep_id)
    witnesses=Witnesses.objects.all().filter(report_id=rep_id)
    return render(request,"police_template/show_witness.html",{"report":report,"witnesses":witnesses})

def view_suspects(request):
    reports=Report.objects.all()
    suspects=Suspects.objects.all()
    counts=[]
    for i in reports:
        count = 0
        for j in suspects:
            if i.id == j.report_id:
                count += 1
        counts.append(count)
    countdict=zip(reports,counts)
    return render(request,"police_template/view_suspects.html",{"reports":reports,"countdict":countdict})

def add_suspects(request,rep_id):
    report=Report.objects.get(id=rep_id)
    return render(request,"police_template/add_suspect.html",{"report":report})

def add_suspects_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        n=int(request.POST.get("number_suspects"))
        for i in range(1,n+1):
            suspect_name=request.POST.get("Suspect_"+str(i)+"_name")
            suspect_email=request.POST.get("Suspect_"+str(i)+"_email")
            suspect_address=request.POST.get("Suspect_"+str(i)+"_address")
            suspect_phonenumber=request.POST.get("Suspect_"+str(i)+"_phonenumber")
            suspect_DOB=request.POST.get("Suspect_"+str(i)+"_DOB")
            suspect_description=request.POST.get("Suspect_"+str(i)+"_description")
            suspect_reason=request.POST.get("Suspect_"+str(i)+"_reason")

            try:
                suspect_model=Suspects(report_id=report_id,name=suspect_name,email=suspect_email,address=suspect_address,
                phone_no=suspect_phonenumber,description=suspect_description,DOB=suspect_DOB,reason=suspect_reason)
                suspect_model.save()
            except:
                messages.error(request,"Failed to add the suspect")
                return HttpResponseRedirect("/add_suspect/"+report_id)
    
        return HttpResponseRedirect("/view_suspects")            

def remove_suspect(request,rep_id):
    report=Report.objects.get(id=rep_id)
    suspects=Suspects.objects.all().filter(report_id=report.id)
    return render(request,"police_template/remove_suspect.html",{"report":report,"suspects":suspects})

def remove_suspect_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        suspect_number=request.POST.get("select_suspect")
        suspect=Suspects.objects.get(id=suspect_number)
        
        try:
            suspect.delete()
            messages.success(request,"Successfully deleted the Suspect")
            return HttpResponseRedirect("/remove_suspect/"+report_id)
        except:
            messages.error(request,"Failed to delete the witness")
            return HttpResponseRedirect("/remove_suspect/"+report_id)
    
def show_suspects(request,rep_id):
    report=Report.objects.get(id=rep_id)
    suspects=Suspects.objects.all().filter(report_id=rep_id)
    return render(request,"police_template/show_suspect.html",{"report":report,"suspects":suspects})

def view_theories(request):
    reports=Report.objects.all()
    theory=Theories.objects.all()
    counts=[]
    for i in reports:
        count = 0
        for j in theory:
            if i.id == j.report_id:
                count += 1
        counts.append(count)
    countdict=zip(reports,counts)
    return render(request,"police_template/view_theories.html",{"reports":reports,"countdict":countdict})

def add_theory(request,rep_id):
    report=Report.objects.get(id=rep_id)
    return render(request,"police_template/add_theory.html",{"report":report})

def add_theory_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        n=int(request.POST.get("number_theory"))
        for i in range(1,n+1):
            Theory_name=request.POST.get("Theory_"+str(i)+"_name")
            Theory_proposedby=request.POST.get("Theory_"+str(i)+"_proposedby")
            Theory_against=request.POST.get("Theory_"+str(i)+"_against")
            Theory_description=request.POST.get("Theory_"+str(i)+"_description")
            Theory_reason=request.POST.get("Theory_"+str(i)+"_reason")

            try:
                theory_model=Theories(report_id=report_id,proposed_by=Theory_proposedby,proposed_by_name=Theory_name,
                against=Theory_against,description=Theory_description,reason=Theory_reason)
                theory_model.save()
            except:
                messages.error(request,"Failed to add the Theory")
                return HttpResponseRedirect("/add_theory/"+report_id)
    
        return HttpResponseRedirect("/view_theories")

def show_theory(request,rep_id):
    report=Report.objects.get(id=rep_id)
    theories=Theories.objects.all().filter(report_id=rep_id)
    return render(request,"police_template/show_theory.html",{"report":report,"theories":theories})

def remove_theory(request,rep_id):
    report=Report.objects.get(id=rep_id)
    theories=Theories.objects.all().filter(report_id=report.id)
    return render(request,"police_template/remove_theory.html",{"report":report,"theories":theories})

def remove_theory_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        select_theory=request.POST.get("select_theory")
        theory=Theories.objects.get(id=select_theory)

        try:
            theory.delete()
            messages.success(request,"Successfully deleted the Theory")
            return HttpResponseRedirect("/remove_theory/"+report_id)
        except:
            messages.error(request,"Failed to delete the Theory")
            return HttpResponseRedirect("/remove_theory/"+report_id)

def view_investigation_all(request):
    report=Report.objects.all().filter(Q(status="Viewed") | Q(status="Filed") | Q(status="Pending"))
    return render(request,"police_template/view_investigation.html",{"report":report})

def view_investigation_allpage(request,page_number):
    rows=request.POST.get("max_rows")
    reports=Report.objects.all()[int(rows)*int(page_number):int(rows)*(int(page_number)+1)]
    length_reports=len(reports)
    p_number=page_number
    return render(request,"police_template/view_investigation_page.html",{"rows":rows,"len_reports":length_reports,"report":reports,"p_number":int(p_number)})

def add_investigation(request,rep_id):
    report=Report.objects.get(id=rep_id)
    police=Police.objects.all()
    try:
        investigation_report=Investigation_Report.objects.get(report_id=rep_id)
        return render(request,"police_template/show_investigation.html",{"report":report,"investigation_report":investigation_report})
    except Investigation_Report.DoesNotExist:
        return render(request,"police_template/add_investigation.html",{"report":report,"police":police})
    

def add_investigation_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        report_id=request.POST.get("report_id")
        legit_report=request.POST.get("legit_report")
        report_scene_address=request.POST.get("report_scene_address")
        report_scene_firstdate=request.POST.get("report_scene_firstdate")
        report_scene_description=request.POST.get("report_scene_description")
        first_officer=request.POST.get("first_officer")
        assisting_officer=request.POST.get("assisting_officer")

        main_witness_name=request.POST.get("main_witness_name")
        main_witness_email=request.POST.get("main_witness_email")
        main_witness_address=request.POST.get("main_witness_address")
        main_witness_phoneno=request.POST.get("main_witness_phoneno")
        main_witness_DOB=request.POST.get("main_witness_DOB")
        main_witness_desc=request.POST.get("main_witness_desc")
        main_witness_blame=request.POST.get("main_witness_blame")

        main_suspect_name=request.POST.get("main_suspect_name")
        main_suspect_email=request.POST.get("main_suspect_email")
        main_suspect_address=request.POST.get("main_suspect_address")
        main_suspect_phoneno=request.POST.get("main_suspect_phoneno")
        main_suspect_DOB=request.POST.get("main_suspect_DOB")
        main_suspect_desc=request.POST.get("main_suspect_desc")
        main_suspect_defense=request.POST.get("main_suspect_defense")

        legit_reason=request.POST.get("legit_reason")      

        try:
            if legit_reason == "No":
                investigation_model=Investigation_Report(report_id=report_id,legit_reason=legit_reason,legit_report=legit_report)
                investigation_model.save()

                report_model=Report.objects.get(id=report_id)
                report_model.status="Dismissed"
                report_model.save()

            elif legit_reason == "Yes":
                investigation_model=Investigation_Report(report_id=report_id,legit_report=legit_report,scene_address=report_scene_address,scene_firstvisited=report_scene_firstdate,
                scene_description=report_scene_description,first_officer=first_officer,assisting_officer=assisting_officer,
                main_witness_name=main_witness_name,main_witness_email=main_witness_email,main_witness_address=main_witness_address,
                main_witness_phone_no=main_witness_phoneno,main_witness_DOB=main_witness_DOB,main_witness_description=main_witness_desc,
                main_witness_blame=main_witness_blame,main_suspect_name=main_suspect_name,main_suspect_email=main_suspect_email,
                main_suspect_address=main_suspect_address,main_suspect_phone_no=main_suspect_phoneno,main_suspect_DOB=main_suspect_DOB,
                main_suspect_description=main_suspect_desc,main_suspect_defense=main_suspect_defense,legit_reason=legit_reason)
                investigation_model.save()
            messages.success(request,"Successfully added the investigation report")
            return HttpResponseRedirect("/show_investigation/"+report_id)
        except:
            messages.error(request,"Failed to add the investigation report")
            return HttpResponseRedirect("/add_investigation/"+report_id)

def show_investigation(request,rep_id):
    report=Report.objects.get(id=rep_id)
    investigation_report=Investigation_Report.objects.get(report_id=rep_id)
    return render(request,"police_template/show_investigation.html",{"report":report,"investigation_report":investigation_report})

def edit_investigation(request,rep_id):
    report=Report.objects.get(id=rep_id)
    police=Police.objects.all()
    investigation_report=Investigation_Report.objects.get(report_id=rep_id)
    return render(request,"police_template/edit_investigation.html",{"report":report,"investigation_report":investigation_report,"police":police})

def edit_investigation_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not allowed</h2>")
    else:
        report_id=request.POST.get("report_id")
        legit_report=request.POST.get("legit_report")
        report_scene_address=request.POST.get("report_scene_address")
        report_scene_firstdate=request.POST.get("report_scene_firstdate")
        report_scene_description=request.POST.get("report_scene_description")
        first_officer=request.POST.get("first_officer")
        assisting_officer=request.POST.get("assisting_officer")

        main_witness_name=request.POST.get("main_witness_name")
        main_witness_email=request.POST.get("main_witness_email")
        main_witness_address=request.POST.get("main_witness_address")
        main_witness_phoneno=request.POST.get("main_witness_phoneno")
        main_witness_DOB=request.POST.get("main_witness_DOB")
        main_witness_desc=request.POST.get("main_witness_desc")
        main_witness_blame=request.POST.get("main_witness_blame")

        main_suspect_name=request.POST.get("main_suspect_name")
        main_suspect_email=request.POST.get("main_suspect_email")
        main_suspect_address=request.POST.get("main_suspect_address")
        main_suspect_phoneno=request.POST.get("main_suspect_phoneno")
        main_suspect_DOB=request.POST.get("main_suspect_DOB")
        main_suspect_desc=request.POST.get("main_suspect_desc")
        main_suspect_defense=request.POST.get("main_suspect_defense")

        legit_reason=request.POST.get("legit_reason")

        try:
            investigation_model=Investigation_Report.objects.get(report_id=report_id)

            investigation_model.report_id=report_id
            investigation_model.legit_report=legit_report
            investigation_model.scene_address=report_scene_address
            investigation_model.scene_firstvisited=report_scene_firstdate
            investigation_model.scene_description=report_scene_description
            investigation_model.first_officer=first_officer
            investigation_model.assisting_officer=assisting_officer
            
            investigation_model.main_witness_name=main_witness_name
            investigation_model.main_witness_email=main_witness_email
            investigation_model.main_witness_address=main_witness_address
            investigation_model.main_witness_phone_no=main_witness_phoneno
            investigation_model.main_witness_DOB=main_witness_DOB
            investigation_model.main_witness_description=main_witness_desc
            investigation_model.main_witness_blame=main_witness_blame
            
            investigation_model.main_suspect_name=main_suspect_name
            investigation_model.main_suspect_email=main_suspect_email
            investigation_model.main_suspect_address=main_suspect_address
            investigation_model.main_suspect_phone_no=main_suspect_phoneno
            investigation_model.main_suspect_DOB=main_suspect_DOB
            investigation_model.main_suspect_description=main_suspect_desc
            investigation_model.main_suspect_defense=main_suspect_defense

            investigation_model.legit_reason=legit_reason
            investigation_model.save()

            messages.success(request,"Successfully edited the investigation report")
            return HttpResponseRedirect("/show_investigation/"+report_id)
        except:
            messages.error(request,"Failed to edit the investigation report")
            return HttpResponseRedirect("/edit_investigation/"+report_id)

def view_investigation_notstarted(request):
    report=Report.objects.all().filter(status="Pending")
    return render(request,"police_template/view_investigation_notstarted.html",{"report":report})

def view_investigation_pending(request):
    report=Report.objects.all().filter(status="Viewed")
    return render(request,"police_template/view_investigation_pending.html",{"report":report})

def view_investigation_completed(request):
    report=Report.objects.all().filter(status="Filed")
    return render(request,"police_template/view_investigation_completed.html",{"report":report})

def view_all_criminals_police(request):
    criminals=Criminal.objects.all().filter(status="Added")
    return render(request,"police_template/view_all_criminal_police.html",{"criminals":criminals})

def view_criminal_details_police(request,criminal_id):
    criminal=Criminal.objects.get(id=criminal_id)
    cell=Cell.objects.get(criminal_id=criminal_id)
    return render(request,"police_template/view_criminal_details_police.html",{"criminal":criminal,"cell":cell})

@csrf_exempt
def get_row_data(request):
    rows=request.POST.get("rows")

    Reports=Report.objects.all().order_by('id')[:int(rows)] 
    Reports_data=serializers.serialize('python',Reports)
    return JsonResponse(json.dumps(Reports_data,default=myconverter),content_type="application/json",safe=False)
