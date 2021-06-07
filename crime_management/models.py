from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils.timezone import now

class CustomUser(AbstractUser):
    user_type_data=((1,"Person"),(2,"Police"),(3,"Admin"),(4,"Court"),(5,"Jail"),(6,"Doctor"))
    user_type=models.CharField(choices=user_type_data,max_length=10,default=3)

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=3,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class RegisterPerson(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=3,on_delete=models.CASCADE)
    nationality=models.CharField(max_length=255,null=True,default=None,blank=True)
    state=models.CharField(max_length=255,null=True,default=None,blank=True)
    Person_DOB=models.DateField(null=True,default=None,blank=True)
    address=models.CharField(max_length=255,null=True,default=None,blank=True)
    phonenumber=models.CharField(max_length=15,null=True,default=None,blank=True)
    objects=models.Manager()  

class Police(models.Model):
    rank_choices=[
        ('PC','police_constable'),
        ('INS','police_inspector'),
        ('ACP','Assistant_commisioner_of_police'),
        ('SP','Superintendent_police')
    ]

    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=3,on_delete=models.CASCADE)
    address=models.CharField(max_length=255,null=True,default=None,blank=True)
    phonenumber=models.CharField(max_length=15,null=True,default=None,blank=True)
    position=models.CharField(max_length=255,null=True,default=None,blank=True,choices=rank_choices)
    DOB=models.DateField(null=True,default=None,blank=True)
    Sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    officer_image=models.FileField(max_length=255,default=None,null=True,blank=True)
    objects=models.Manager()  

class Court(models.Model):
    court_choices=[
        ('High_Court','High_Court'),
        ('District_Court', 'District_Court'),
        ('Lower_Court','Lower_Court')
    ]
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=3,on_delete=models.CASCADE)
    address=models.CharField(max_length=255,null=True,default=None,blank=True)
    phonenumber=models.CharField(max_length=15,null=True,default=None,blank=True)
    created_at=models.DateTimeField(default=now,blank=True,null=True)
    court_type=models.CharField(choices=court_choices,max_length=255,null=True,default=None,blank=True)
    objects=models.Manager()  

class Jail(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=3,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=now)
    jail_name=models.CharField(max_length=255,null=True,default=None,blank=True)
    jail_email=models.CharField(max_length=255,null=True,default=None,blank=True)
    address=models.CharField(max_length=255,null=True,default=None,blank=True)
    phonenumber=models.CharField(max_length=15,null=True,default=None,blank=True)
    jailer=models.CharField(max_length=255,null=True,default=None,blank=True)
    description=models.TextField(default=None,null=True,blank=True)
    objects=models.Manager()

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,default=3,on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=255,null=True,default=None,blank=True)
    doctor_email=models.CharField(max_length=255,null=True,default=None,blank=True)
    created_at=models.DateTimeField(default=now)
    address=models.CharField(max_length=255,null=True,default=None,blank=True)
    phonenumber=models.CharField(max_length=15,null=True,default=None,blank=True)
    DOB=models.DateField(null=True,default=None,blank=True)
    image=models.FileField(max_length=255,default=None,null=True,blank=True)
    sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    objects=models.Manager()

class Report(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(default=now,blank=True,null=True)
    updated_at=models.DateTimeField(default=now,blank=True,null=True)
    person_id=models.IntegerField(default=0,blank=True,null=True)

    report_by_type=models.CharField(max_length=255,null=True,default=None,blank=True,choices=[('Person','Person'),('Organization','Organization')])
    inf_name=models.CharField(max_length=255,null=True,default=None,blank=True)
    inf_email=models.CharField(max_length=255,null=True,default=None,blank=True)
    inf_sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other'),('NA','NA')],default='M',null=True,blank=True)
    inf_address=models.CharField(max_length=255,null=True,default=None,blank=True)
    inf_phonenumber=models.CharField(max_length=255,null=True,default=None,blank=True)
    inf_image=models.FileField(max_length=255,default=None,null=True,blank=True)

    reportagainst=models.CharField(max_length=255,null=True,default=None,blank=True,choices=[('Person','Person'),('Organization','Organization')])
    reportagainst_name=models.CharField(max_length=255,null=True,default=None,blank=True)
    reportagainst_email=models.CharField(max_length=255,null=True,default=None,blank=True)
    reportagainst_address=models.CharField(max_length=255,null=True,default=None,blank=True)
    reportagainst_phonenumber=models.CharField(max_length=255,null=True,default=None,blank=True)
    reportagainstsex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other'),('NA','NA')],default='M',null=True,blank=True)
    
    eventdate=models.DateField(default=now,null=True,blank=True)
    eventtype=models.CharField(max_length=255,null=True,default=None,blank=True)
    eventaddress=models.CharField(max_length=255,null=True,default=None,blank=True)
    eventdescription=models.TextField(default=None,null=True,blank=True)
    reportagainst_image=models.FileField(max_length=255,default=None,null=True,blank=True)

    status=models.CharField(max_length=255,choices=[('Pending','Pending'),('Viewed','Viewed'),('Filed','Filed'),('Dismissed','Dismissed')],default='Pending',null=True,blank=True)
    objects=models.Manager()

class Investigation_Report(models.Model):
    id=models.AutoField(primary_key=True)
    report_id=models.IntegerField(default=None,blank=True,null=True)
    created_at=models.DateTimeField(default=now,blank=True,null=True)
    legit_report=models.CharField(max_length=255,choices=[('Yes','Yes'),('No','No')],default=None,blank=True,null=True)
            
    scene_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    scene_firstvisited=models.DateTimeField(default=None,blank=True,null=True)
    scene_description=models.TextField(default=None,blank=True,null=True)
    first_officer=models.CharField(max_length=255,default=None,blank=True,null=True)
    assisting_officer=models.CharField(max_length=255,default=None,blank=True,null=True)

    main_witness_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    main_witness_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    main_witness_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    main_witness_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    main_witness_DOB=models.DateField(default=None,blank=True,null=True)   
    main_witness_description=models.TextField(default=None,blank=True,null=True)
    main_witness_blame=models.TextField(max_length=255,default=None,blank=True,null=True)

    main_suspect_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    main_suspect_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    main_suspect_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    main_suspect_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    main_suspect_DOB=models.DateField(default=None,blank=True,null=True)    
    main_suspect_description=models.TextField(default=None,blank=True,null=True)
    main_suspect_defense=models.TextField(default=None,blank=True,null=True)

    legit_reason=models.TextField(default=None,blank=True,null=True)

    objects=models.Manager()



class Suspects(models.Model):
    report_id=models.IntegerField(default=None,blank=True,null=True)
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(default=now)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,default=None,blank=True,null=True)
    address=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=15)
    DOB=models.DateField(default=now,blank=True,null=True)    
    description=models.TextField(default=None,blank=True,null=True)
    reason=models.TextField()
    objects=models.Manager()

class Witnesses(models.Model):
    report_id=models.IntegerField(default=None,blank=True,null=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,default=None,blank=True,null=True)
    address=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=15)
    created_at=models.DateTimeField(default=now)
    description=models.TextField()
    DOB=models.DateField(default=now,blank=True,null=True)
    objects=models.Manager()

class Theories(models.Model):
    report_id=models.IntegerField(default=None,blank=True,null=True)
    id=models.AutoField(primary_key=True)  
    created_at=models.DateTimeField(default=now)
    proposed_by=models.CharField(max_length=255,choices=[('Witness','Witness'),('Police','Police')],blank=True,null=True,default=None)
    proposed_by_name=models.CharField(max_length=255,blank=True,null=True,default=None)
    against=models.CharField(max_length=255,blank=True,null=True,default=None)
    description=models.TextField()
    reason=models.TextField(blank=True,null=True,default=None)
    objects=models.Manager()

class ChargeSheet(models.Model):
    id=models.AutoField(primary_key=True)
    charging_officer=models.CharField(max_length=255,default="username",null=True,blank=True)
    report_id=models.IntegerField(default=None,blank=True,null=True)

    #Accused person details
    Accused_name=models.CharField(max_length=255,default=None,null=True,blank=True)
    Accused_address=models.CharField(max_length=255,default=None,null=True,blank=True)
    Accused_phone_no=models.CharField(max_length=15,default=None,null=True,blank=True)
    Accused_email=models.CharField(max_length=255,default=None,null=True,blank=True)
    Accused_sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    Accused_Charges=models.TextField(default=None)
    Accused_DOB=models.DateField(default=None)
    Accused_underwhatlaw=models.CharField(max_length=10,choices=[('State','State'),('Act','Act'),('Cwealth','CWealth'),('Reg','Reg'),('Other','Other')],default='State',null=True,blank=True)
    Accused_typeofoffense=models.CharField(max_length=20,choices=[('SO','Summary offense'),('IO','Indictable offense')],default='SO',null=True,blank=True)
    Accused_Act=models.CharField(max_length=5,default=None,null=True,blank=True)
    Accused_section=models.CharField(max_length=100,default=None,null=True,blank=True)
    Accused_image=models.FileField(max_length=255,default=None,null=True,blank=True)
    
    #Informant details
    Informant_name=models.CharField(max_length=255,default=None,null=True,blank=True)
    Informant_address=models.CharField(max_length=255,default=None,null=True,blank=True)
    Informant_phone_no=models.CharField(max_length=15,default=None,null=True,blank=True)
    Informant_email=models.CharField(max_length=255,default=None,null=True,blank=True)
    Informant_description=models.TextField(default=None,null=True,blank=True)
    Informant_DOB=models.DateField(default=None)
    Informant_sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    Informant_initial_report=models.DateField(default=now,null=True,blank=True)
    Informant_image=models.FileField(max_length=255,default=None,null=True,blank=True)
    Informant_signature=models.FileField(max_length=255,default=None,null=True,blank=True)
    
    #Other details
    Reporting_officer=models.CharField(max_length=255,default=None,null=True,blank=True)
    Investigation_officer=models.CharField(max_length=255,default=None,null=True,blank=True)
    Assisting_officer=models.CharField(max_length=255,default=None,null=True,blank=True)
    Issued_at=models.CharField(max_length=255,default=None,null=True,blank=True)
    Issued_when=models.DateTimeField(default=now,null=True,blank=True)
    Investigation_details=models.TextField(default=None,null=True,blank=True)

    #Theories
    Theories=models.IntegerField(null=True,default=None,blank=True)
    Theory1=models.TextField(null=True,default=None,blank=True)
    Theory2=models.TextField(null=True,default=None,blank=True)
    Theory3=models.TextField(null=True,default=None,blank=True)
    Theory4=models.TextField(null=True,default=None,blank=True)
    Theory5=models.TextField(null=True,default=None,blank=True)

    #Witnesses
    Witnesses=models.IntegerField(null=True,default=None,blank=True)
    Witness1=models.TextField(null=True,default=None,blank=True)
    Witness2=models.TextField(null=True,default=None,blank=True)
    Witness3=models.TextField(null=True,default=None,blank=True)
    Witness4=models.TextField(null=True,default=None,blank=True)
    Witness5=models.TextField(null=True,default=None,blank=True)

    #Suspects
    Suspects=models.IntegerField(null=True,default=None,blank=True)
    Suspect1=models.TextField(null=True,default=None,blank=True)
    Suspect2=models.TextField(null=True,default=None,blank=True)
    Suspect3=models.TextField(null=True,default=None,blank=True)
    Suspect4=models.TextField(null=True,default=None,blank=True)
    Suspect5=models.TextField(null=True,default=None,blank=True)

    status=models.CharField(max_length=255,choices=[('Pending','Pending'),('Completed','Completed')],default='Pending',blank=True,null=True)
    objects=models.Manager()

class Attorney(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(default=now)
    name=models.CharField(max_length=255,default=None,blank=True,null=True)
    email=models.CharField(max_length=255,default=None,blank=True,null=True)
    address=models.CharField(max_length=255,default=None,blank=True,null=True)
    phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    Sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    DOB=models.DateField(default=now,blank=True,null=True)

    objects=models.Manager()

class Judge(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(default=now)
    name=models.CharField(max_length=255,default=None,blank=True,null=True)
    email=models.CharField(max_length=255,default=None,blank=True,null=True)
    address=models.CharField(max_length=255,default=None,blank=True,null=True)
    phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    Sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    DOB=models.DateField(default=now,blank=True,null=True)

    objects=models.Manager()

class Case(models.Model):
    id=models.AutoField(primary_key=True)
    charge_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    #hearing time and court details
    court_choices=[
        ('High_Court','High_Court'),
        ('District_Court', 'District_Court'),
        ('Lower_Court','Lower_Court')
    ]
    court_name=models.CharField(max_length=255,null=True,blank=True,default=None)
    court_address=models.CharField(max_length=255,null=True,blank=True,default=None)
    court_type=models.CharField(choices=court_choices,max_length=255,null=True,default=None,blank=True)
    final_hearing=models.DateTimeField(default=now,null=True,blank=True)
    first_hearing=models.DateTimeField(default=now,null=True,blank=True)

    #defending attorney
    def_id=models.IntegerField(default=None,blank=True,null=True)
    def_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    def_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    def_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    def_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    def_DOB=models.DateField(default=None,blank=True,null=True)

    #prosecuting attorney
    pros_id=models.IntegerField(default=None,blank=True,null=True)
    pros_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    pros_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    pros_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    pros_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    pros_DOB=models.DateField(default=None,blank=True,null=True)

    #defending person/entity
    crime_choices=[
        ('Personal_crime','Personal_crime'),
        ('Property_crime','Property_crime'),
        ('Inchoate_crime','Inchoate_crime'),
        ('Statutory_crime','Statutory_crime'),
        ('Financial_crime','Financial_crime'),
        ('Other_crime','Other_crime')
    ]

    def_person_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    def_person_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    def_person_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    def_person_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)    
    def_crime_type=models.CharField(max_length=255,default=None,blank=True,null=True,choices=crime_choices)
    def_person_DOB=models.DateField(default=None,blank=True,null=True)
    def_person_charges=models.TextField(default=None,blank=True,null=True)
    def_person_image=models.FileField(default=None,blank=True,null=True)    

    #prosecuting person/entity
    pros_person_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    pros_person_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    pros_person_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    pros_person_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    pros_person_DOB=models.DateField(default=None,blank=True,null=True)
    pros_person_desc=models.TextField(default=None,blank=True,null=True)
    pros_person_image=models.FileField(default=None,blank=True,null=True)

    #judge details
    judge_id=models.IntegerField(default=None,blank=True,null=True)
    judge_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    judge_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    judge_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    judge_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    judge_DOB=models.DateField(default=None,blank=True,null=True)        

    status=models.CharField(max_length=255,choices=[('Pending','Pending'),('Completed','Completed')],default='Pending',blank=True,null=True)
    objects=models.Manager()

class Decision(models.Model):
    id=models.AutoField(primary_key=True)
    case_id=models.IntegerField(default=None,null=True,blank=True)
    criminal_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    decision=models.CharField(max_length=255,choices=[('Yes','Yes'),('No','No')],default=None,null=True,blank=True)
    decision_reason=models.TextField(default=None,null=True,blank=True)
    decision_desc=models.TextField(default=None,null=True,blank=True)

    objects=models.Manager()

class Criminal(models.Model):
    id=models.AutoField(primary_key=True)
    decision_id=models.IntegerField(default=None,null=True,blank=True)
    case_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)
    
    #criminal details
    criminal_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    criminal_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    criminal_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    criminal_phone_no=models.CharField(max_length=15,default=None,blank=True,null=True)
    criminal_DOB=models.DateField(default=None,blank=True,null=True)
    criminal_sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    criminal_image=models.FileField(default=None,blank=True,null=True)
    criminal_charges=models.TextField(default=None,blank=True,null=True)
    criminal_sentence_duration=models.CharField(max_length=255,default=None,blank=True,null=True)
    criminal_sentence_start=models.DateField(default=None,blank=True,null=True)
    criminal_sentence_end=models.DateField(default=None,blank=True,null=True)

    #crime details
    crime_choices=[
        ('Personal_crime','Personal_crime'),
        ('Property_crime','Property_crime'),
        ('Inchoate_crime','Inchoate_crime'),
        ('Statutory_crime','Statutory_crime'),
        ('Financial_crime','Financial_crime'),
        ('Other_crime','Other_crime')
    ]
    crime_type=models.CharField(max_length=255,default=None,blank=True,null=True,choices=crime_choices)
    crime_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    crime_desc=models.TextField(default=None,blank=True,null=True)
    crime_date=models.DateTimeField(default=None,blank=True,null=True)
    crime_place=models.CharField(max_length=255,default=None,blank=True,null=True)

    #jail_details
    jail_id=models.IntegerField(default=None,null=True,blank=True)
    jail_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_jailer=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_phoneno=models.CharField(max_length=255,default=None,blank=True,null=True)

    status_health_record=models.CharField(choices=[('Uploaded','Uploaded'),('Not_Uploaded','Not_Uploaded')],max_length=255,default='Not_Uploaded',blank=True,null=True)
    status_work=models.CharField(choices=[('Alloted','Alloted'),('Not_Alloted','Not_Alloted')],max_length=255,default='Not_Alloted',blank=True,null=True)
    status=models.CharField(choices=[('Sent','Sent'),('Added','Added'),('Released','Released')],max_length=255,default='Sent',blank=True,null=True)
    objects=models.Manager()

class Crime(models.Model):
    id=models.AutoField(primary_key=True)
    criminal_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    crime_choices=[
        ('Personal_crime','Personal_crime'),
        ('Property_crime','Property_crime'),
        ('Inchoate_crime','Inchoate_crime'),
        ('Statutory_crime','Statutory_crime'),
        ('Financial_crime','Financial_crime'),
        ('Other_crime','Other_crime')
    ]
    crime_type=models.CharField(max_length=255,default=None,blank=True,null=True,choices=crime_choices)
    crime_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    crime_desc=models.TextField(default=None,blank=True,null=True)
    crime_date=models.DateTimeField(default=None,blank=True,null=True)
    crime_place=models.CharField(max_length=255,default=None,blank=True,null=True)
    created_at=models.DateTimeField(default=now)

    objects=models.Manager()

class Cell(models.Model):
    cell_choices=[
        ('NC','normal_cell'),
        ('HSC','High_Security_cell'),
        ('IC','Isolation_cell'),
        ('EC','Execution_cell'),
    ]

    id=models.AutoField(primary_key=True)
    criminal_id=models.IntegerField(default=0,null=True,blank=True)
    jail_id=models.IntegerField(default=0,null=True,blank=True)
    created_at=models.DateTimeField(default=now)    

    cell_type=models.CharField(max_length=255,default=None,blank=True,null=True,choices=cell_choices)
    cell_section=models.CharField(max_length=255,default=None,blank=True,null=True)
    cell_number=models.CharField(max_length=255,default=None,blank=True,null=True)    
    
    objects=models.Manager()

class Work(models.Model):
    work_choices=[
        ('Agriculture','Agriculture'),
        ('Mining','Mining'),
        ('Construction','Construction'),
        ('Prison_support','Prison_support'),
    ]

    id=models.AutoField(primary_key=True)
    criminal_id=models.IntegerField(default=0,null=True,blank=True)
    jail_id=models.IntegerField(default=0,null=True,blank=True)
    created_at=models.DateTimeField(default=now)
    
    work_type=models.CharField(max_length=255,default=None,blank=True,null=True,choices=work_choices)
    work_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    work_desc=models.TextField(default=None,blank=True,null=True)
    work_duration=models.CharField(max_length=255,default=None,blank=True,null=True)
    work_start_time=models.TimeField(default=now,blank=True,null=True)
    work_end_time=models.TimeField(default=now,blank=True,null=True)

    objects=models.Manager()

class Release(models.Model):
    id=models.AutoField(primary_key=True)
    case_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    release_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    release_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    release_phone_no=models.CharField(max_length=255,default=None,blank=True,null=True)
    release_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    release_DOB=models.DateField(default=None,blank=True,null=True)
    release_sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other'),('NA','NA')],default='M',null=True,blank=True)
    release_dropcharges=models.TextField(default=None,blank=True,null=True)
    release_date=models.DateField(default=now,blank=True,null=True)
    release_time=models.TimeField(default=now,blank=True,null=True)
    release_place=models.CharField(max_length=255,default=None,blank=True,null=True)
    release_type=models.CharField(choices=[('Convicted','Convicted'),('Innocent','Innocent')],max_length=255,default=None,blank=True,null=True)
    release_image=models.FileField(max_length=255,default=None,null=True,blank=True)

    objects=models.Manager()

class HealthRecord(models.Model):
    id=models.AutoField(primary_key=True)
    criminal_id=models.IntegerField(default=None,null=True,blank=True)
    criminal_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_id=models.IntegerField(default=None,null=True,blank=True)
    doctor_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    previous_diseases=models.TextField(default=None,null=True,blank=True)
    family_diseases=models.TextField(default=None,blank=True,null=True)
    allergies=models.TextField(default=None,blank=True,null=True)
    current_medications=models.TextField(default=None,blank=True,null=True)
    current_diseases=models.TextField(default=None,blank=True,null=True)

    height=models.IntegerField(default=0,null=True,blank=True)
    weight=models.IntegerField(default=0,null=True,blank=True)
    BMI=models.IntegerField(default=0,null=True,blank=True)
    BP=models.IntegerField(default=0,null=True,blank=True)
    Hearing=models.CharField(max_length=255,default=None,blank=True,null=True)
    Vision=models.CharField(max_length=255,default=None,blank=True,null=True)
    Dental=models.CharField(max_length=255,default=None,blank=True,null=True)

    x_ray_results=models.TextField(default=None,blank=True,null=True)
    x_ray_report=models.FileField(max_length=255,default=None,null=True,blank=True)
    abornmalities=models.TextField(default=None,blank=True,null=True)
    mental_report=models.TextField(default=None,blank=True,null=True)    

    signature=models.FileField(max_length=255,default=None,null=True,blank=True)

    objects=models.Manager()

class MonthlyCheckup(models.Model):
    id=models.AutoField(primary_key=True)
    criminal_id=models.IntegerField(default=None,null=True,blank=True)
    criminal_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_id=models.IntegerField(default=None,null=True,blank=True)
    doctor_id=models.IntegerField(default=None,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    weight=models.IntegerField(default=0,null=True,blank=True)
    BMI=models.IntegerField(default=0,null=True,blank=True)
    BP=models.IntegerField(default=0,null=True,blank=True)
    Hearing=models.CharField(max_length=255,default=None,blank=True,null=True)
    Vision=models.CharField(max_length=255,default=None,blank=True,null=True)
    Dental=models.CharField(max_length=255,default=None,blank=True,null=True)
    MentalHealth=models.TextField(default=None,null=True,blank=True)
    Injuries=models.TextField(default=None,null=True,blank=True)
    Medications=models.TextField(default=None,null=True,blank=True)

    objects=models.Manager()

class Meeting(models.Model):
    id=models.AutoField(primary_key=True)
    criminal_id=models.IntegerField(default=None,null=True,blank=True)
    criminal_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    jail_id=models.IntegerField(default=None,null=True,blank=True)
    person_id=models.IntegerField(default=0,null=True,blank=True)
    created_at=models.DateTimeField(default=now)

    meeting_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    meeting_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    meeting_email=models.CharField(max_length=255,default=None,blank=True,null=True)
    meeting_DOB=models.DateField(default=None,blank=True,null=True)
    meeting_sex=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('Oth','Other')],default='M',null=True,blank=True)
    meeting_phonenumber=models.CharField(max_length=15,default=None,blank=True,null=True)
    meeting_image=models.FileField(max_length=255,default=None,null=True,blank=True)

    occupation_type=models.CharField(max_length=255,default=None,blank=True,null=True)
    occupation_name=models.CharField(max_length=255,default=None,blank=True,null=True)
    occupation_address=models.CharField(max_length=255,default=None,blank=True,null=True)
    occupation_phonenumber=models.CharField(max_length=255,default=None,blank=True,null=True)

    meeting_date=models.DateField(default=None,blank=True,null=True)
    meeting_actual_date=models.DateField(default=None,blank=True,null=True)
    meeting_start_time=models.TimeField(default=None,blank=True,null=True)
    meeting_end_time=models.TimeField(default=None,blank=True,null=True)
    meeting_room=models.CharField(max_length=255,default=None,blank=True,null=True)
    criminal_relation=models.CharField(max_length=255,default=None,blank=True,null=True)
    criminal_reason=models.TextField(default=None,null=True,blank=True)
    reject_reason=models.TextField(default=None,null=True,blank=True)
    status=models.CharField(choices=[('Pending','Pending'),('Granted','Granted'),('Denied','Denied')],max_length=255,default='Pending',blank=True,null=True)

    objects=models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            RegisterPerson.objects.create(admin=instance)
        if instance.user_type==2:
            Police.objects.create(admin=instance)
        if instance.user_type==3:
            Admin.objects.create(admin=instance)
        if instance.user_type==4:
            Court.objects.create(admin=instance)
        if instance.user_type==5:
            Jail.objects.create(admin=instance)
        if instance.user_type==6:
            Doctor.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.registerperson.save()
    if instance.user_type==2:
        instance.police.save()
    if instance.user_type==3:
        instance.admin.save()
    if instance.user_type==4:
        instance.court.save()
    if instance.user_type==5:
        instance.jail.save()
    if instance.user_type==6:
        instance.doctor.save()
