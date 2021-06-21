"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from crime_management import views,PoliceViews,PersonViews,AdminViews,CourtViews,JailViews,DoctorViews
from django.conf import settings



urlpatterns = [
    path('index',views.showdemopage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.LogoutUser,name="logout_user"),
    path('doLogin',views.doLogin,name="dologin"),
    path('login_test',views.showlogin_test),

#police urls
    path('police_home',PoliceViews.police_home,name="police_home"),
    path('view_charge_sheets',PoliceViews.view_charge_sheets,name="view_charge_sheets"),
    path('Charge_Sheet/<str:rep_id>',PoliceViews.Charge_sheet,name="Charge_Sheet"),
    path('Charge_Sheet_save',PoliceViews.Charge_sheet_save),
    path('Register',views.ViewRegister,name="Register"),
    path('do_person_register',views.do_person_register),
    path('view_report_all',PoliceViews.view_report_all),
    path('edit_report/<str:rep_id>', PoliceViews.edit_report),
    path('edit_report_save',PoliceViews.edit_report_save),
    path('police_account',PoliceViews.police_account,name="police_account"),
    path('police_account_save',PoliceViews.police_account_save,name="police_account_save"),
    path('view_completed_report',PoliceViews.view_completed_report),
    path('view_dismissed_report',PoliceViews.view_dismissed_report),
    path('view_all_criminals_police',PoliceViews.view_all_criminals_police,name="view_all_criminals_police"),
    path('view_criminal_details_police/<str:criminal_id>',PoliceViews.view_criminal_details_police,name="view_criminal_details_police"),

    #report_witnesses
    path('view_witnesses',PoliceViews.view_witnesses),
    path('add_witness/<str:rep_id>',PoliceViews.add_witness),
    path('add_witness_save',PoliceViews.add_witness_save),
    path('remove_witness/<str:rep_id>',PoliceViews.remove_witness),
    path('remove_witness_save',PoliceViews.remove_witness_save),
    path('show_witness/<str:rep_id>',PoliceViews.show_witness),

    #report_suspects
    path('view_suspects',PoliceViews.view_suspects),
    path('add_suspect/<str:rep_id>',PoliceViews.add_suspects),
    path('add_suspects_save',PoliceViews.add_suspects_save),
    path('show_suspects/<str:rep_id>',PoliceViews.show_suspects),
    path('remove_suspect/<str:rep_id>',PoliceViews.remove_suspect),
    path('remove_suspect_save',PoliceViews.remove_suspect_save),

    #report_theories
    path('view_theories',PoliceViews.view_theories),
    path('add_theory/<str:rep_id>',PoliceViews.add_theory),
    path('add_theory_save',PoliceViews.add_theory_save), 
    path('show_theory/<str:rep_id>',PoliceViews.show_theory),
    path('remove_theory/<str:rep_id>',PoliceViews.remove_theory),
    path('remove_theory_save',PoliceViews.remove_theory_save), 

    #investigation
    path('view_investigation_all',PoliceViews.view_investigation_all),
    path('add_investigation/<str:rep_id>',PoliceViews.add_investigation),
    path('add_investigation_save',PoliceViews.add_investigation_save),
    path('show_investigation/<str:rep_id>',PoliceViews.show_investigation), 
    path('edit_investigation/<str:rep_id>',PoliceViews.edit_investigation),
    path('edit_investigation_save',PoliceViews.edit_investigation_save),
    path('view_investigation_notstarted',PoliceViews.view_investigation_notstarted),
    path('view_investigation_pending',PoliceViews.view_investigation_pending),
    path('view_investigation_completed',PoliceViews.view_investigation_completed),
    path('view_investigation_all/page/<str:page_number>',PoliceViews.view_investigation_allpage),
    path('get_row_data',PoliceViews.get_row_data, name="get_row_data"),

#person urls
    path('person_home',PersonViews.person_home,name="person_home"),
    path('report_save',PersonViews.report_save,name="report_save"),
    path('arrange_meeting',PersonViews.arrange_meeting,name="arrange_meeting"),
    path('arrange_meeting_save',PersonViews.arrange_meeting_save,name="arrange_meeting_save"),
    path('get_criminal_meeting',PersonViews.get_criminal_meeting,name="get_criminal_meeting"),
    path('view_previous_reports',PersonViews.view_previous_reports,name="view_previous_reports"),
    path('view_report/<str:report_id>',PersonViews.view_report,name="view_report"),
    path('view_all_meetings',PersonViews.view_all_meetings,name="view_all_meetings"),
    path('view_meet_details/<str:meeting_id>',PersonViews.view_meet_details,name="view_meet_details"),
    
#admin urls
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    path('add_police',AdminViews.add_police,name="add_police"),
    path('add_police_save',AdminViews.add_police_save,name="add_police_save"),
    path('remove_police',AdminViews.remove_police,name="remove_police"),
    path('remove_police_save',AdminViews.remove_police_save,name="remove_police_save"),
    path('view_police',AdminViews.view_police,name="view_police"),
    path('edit_police/<str:police_id>',AdminViews.edit_police,name="edit_police"),
    path('edit_police_save',AdminViews.edit_police_save,name="edit_police_save"),
    path('add_court',AdminViews.add_court,name="add_court"),
    path('add_court_save',AdminViews.add_court_save,name="add_court_save"),
    path('remove_court',AdminViews.remove_court,name="remove_court"),
    path('remove_court_save',AdminViews.remove_court_save,name="remove_court_save"),
    path('view_courts',AdminViews.view_courts,name="view_courts"),
    path('edit_court/<str:court_id>',AdminViews.edit_court,name="edit_court"),
    path('edit_court_save',AdminViews.edit_court_save,name="edit_court_save"),
    path('add_jail',AdminViews.add_jail,name="add_jail"),
    path('add_jail_save',AdminViews.add_jail_save,name="add_jail_save"),
    path('remove_jail',AdminViews.remove_jail,name="remove_jail"),
    path('remove_jail_save',AdminViews.remove_jail_save,name="remove_jail_save"),
    path('view_jail',AdminViews.view_jail,name="view_jail"),
    path('edit_jail/<str:jail_id>',AdminViews.edit_jail,name="edit_jail"),
    path('edit_jail_save',AdminViews.edit_jail_save,name="edit_jail_save"),
    path('add_doctor',AdminViews.add_doctor,name="add_doctor"),
    path('add_doctor_save',AdminViews.add_doctor_save,name="add_doctor_save"),
    path('remove_doctor',AdminViews.remove_doctor,name="remove_doctor"),
    path('remove_doctor_save',AdminViews.remove_doctor_save,name="remove_doctor_save"),
    path('view_doctor',AdminViews.view_doctor,name="view_doctor"),
    path('edit_doctor/<str:doctor_id>',AdminViews.edit_doctor,name="edit_doctor"),
    path('edit_doctor_save',AdminViews.edit_doctor_save,name="edit_doctor_save"),
    

#Court urls
    path('court_home',CourtViews.court_home,name="court_home"),
    path('court_account',CourtViews.court_account,name="court_account"),
    path('court_account_save',CourtViews.court_account_save,name="court_account_save"),
    path('view_chargesheets',CourtViews.view_chargesheets,name="view_chargesheets"),
    path('show_chargesheet/<str:charge_id>',CourtViews.show_chargesheet,name="show_chargesheet"),
    path('add_case/<str:charge_id>',CourtViews.add_case,name="add_case"),
    path('add_case_save',CourtViews.add_case_save,name="add_case_save"),
    path('add_attorney',CourtViews.add_attorney,name="add_attorney"),
    path('add_attorney_save',CourtViews.add_attorney_save,name="add_attorney_save"),
    path('view_attorney',CourtViews.view_attorney,name="view_attorney"),
    path('add_judge',CourtViews.add_judge,name="add_judge"),
    path('add_judge_save',CourtViews.add_judge_save,name="add_judge_save"),
    path('view_judge',CourtViews.view_judge,name="view_judge"),
    path('get_def_att_info',CourtViews.get_def_att_info,name="get_def_att_info"),
    path('get_judge_info',CourtViews.get_judge_info,name="get_judge_info"),
    path('view_all_cases',CourtViews.view_all_cases,name="view_all_cases"),
    path('view_case/<str:case_id>',CourtViews.view_case,name="view_case"),
    path('edit_case/<str:case_id>',CourtViews.edit_case,name="edit_case"),
    path('edit_case_save',CourtViews.edit_case_save,name="edit_case_save"),
    path('make_decision/<str:case_id>',CourtViews.make_decision,name="make_decision"),
    path('make_decision_save',CourtViews.make_decision_save,name="make_decision_save"),
    path('add_criminal/<str:case_id>',CourtViews.add_criminal,name="add_criminal"),
    path('add_criminal_save',CourtViews.add_criminal_save,name="add_criminal_save"),
    path('view_all_criminals',CourtViews.view_all_criminals,name="view_all_criminals"),
    path('get_jail_info',CourtViews.get_jail_info,name="get_jail_info"),
    path('add_release/<str:case_id>',CourtViews.add_release,name="add_release"),
    path('add_release_save',CourtViews.add_release_save,name="add_release_save"),
    path('view_all_releases',CourtViews.view_all_releases,name="view_all_releases"),

#Jail urls
    path('jail_home',JailViews.jail_home,name="jail_home"),
    path('jail_account',JailViews.jail_account,name="jail_account"),
    path('jail_account_save',JailViews.jail_account_save,name="jail_account_save"),
    path('view_not_alloted',JailViews.view_not_alloted,name="view_not_alloted"),
    path('add_cell',JailViews.add_cell,name="add_cell"),
    path('add_cell_save',JailViews.add_cell_save,name="add_cell_save"),
    path('view_all_cell',JailViews.view_all_cell,name="view_all_cell"),
    path('edit_cell/<str:cell_id>',JailViews.edit_cell,name="edit_cell"),
    path('edit_cell_save',JailViews.edit_cell_save,name="edit_cell_save"),
    path('remove_cell/<str:cell_id>',JailViews.remove_cell,name="remove_cell"),
    path('view_all_criminal',JailViews.view_all_criminal,name="view_all_criminal"),
    path('view_criminal_details/<str:criminal_id>',JailViews.view_criminal_details,name="view_criminal_details"),
    path('allot_cell/<str:criminal_id>',JailViews.allot_cell,name="allot_cell"),
    path('allot_cell_save',JailViews.allot_cell_save,name="allot_cell_save"),
    path('get_cell_info',JailViews.get_cell_info,name="get_cell_info"),
    path('view_alloted',JailViews.view_alloted,name="view_alloted"),
    path('release_criminal/<str:criminal_id>',JailViews.release_criminal,name="release_criminal"),
    path('release_criminal_save',JailViews.release_criminal_save,name="release_criminal_save"),
    path('assign_work',JailViews.assign_work,name="assign_work"),
    path('get_criminal_info',JailViews.get_criminal_info,name="get_criminal_info"),
    path('assign_work_save',JailViews.assign_work_save,name="assign_work_save"),
    path('view_all_work',JailViews.view_all_work,name="view_all_work"),
    path('view_healthrecord',JailViews.view_healthrecord,name="view_healthrecord"),
    path('get_all_info',JailViews.get_all_info,name="get_all_info"),
    path('view_new_meeting',JailViews.view_new_meeting,name="view_new_meeting"),
    path('view_meeting_details/<str:meeting_id>',JailViews.view_meeting_details,name="view_meeting_details"),
    path('meeting_grant/<str:meeting_id>',JailViews.meeting_grant,name="meeting_grant"),
    path('grant_meeting_save',JailViews.grant_meeting_save,name="grant_meeting_save"),
    path('meeting_reject/<str:meeting_id>',JailViews.meeting_reject,name="meeting_reject"),
    path('view_past_meetings',JailViews.view_past_meetings,name="view_past_meetings"),
    path('view_past_meeting_details/<str:meeting_id>',JailViews.view_past_meeting_details,name="view_past_meeting_details"),
    path('reject_meeting_save',JailViews.reject_meeting_save,name="reject_meeting_save"),
    path('view_released',JailViews.view_released,name="view_released"),

#Doctor urls
    path('doctor_home',DoctorViews.doctor_home,name="doctor_home"),
    path('add_health_record',DoctorViews.add_health_record,name="add_health_record"),
    path('doc_criminal_info',DoctorViews.doc_criminal_info,name="doc_criminal_info"),
    path('add_health_record_save',DoctorViews.add_health_record_save,name="add_health_record_save"),
    path('view_all_health_record',DoctorViews.view_all_health_record,name="view_all_health_record"),
    path('edit_health_record/<str:healthrecord_id>',DoctorViews.edit_health_record,name="edit_health_record"),
    path('edit_health_record_save',DoctorViews.edit_health_record_save,name="edit_health_record_save"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
