
# DBMS Project - Crime Records Management System

Crime Records Management System is a web application that registers complaints and stores all the backend data of all complaints and the action taken by authorities based on that complaint.

# Working

The System is widely divided into five sections consisting of 
-	Person
-	Police
-	Court
-	Jail
-	Doctor  

The five sections depicts the entire process from filing a report to release a criminal after his sentence. 
Whenever a crime is committed, the person/persons/organization can report the crime through this system. The report will then be sent to the police section, where police authorities can view the report and carry out appropriate investigation based on the report. Police may find suspects, witnesses and come up with theories for the event which are essentially the required things during an investigation. If the report turns out to be false then it will be rejected and the investigation will stop, otherwise if the guilty party is found then a chargesheet will be filed against him/her/them.

Court can view the chargesheets based on police investigation and file a case based on it. The Court also manages attorneys and judges for every case and therefore keeps their record as well. The case outcome will come out as a decision of whether the person/persons/organization is found guilty or not. If not found guilty then he/she/them will be released. Otherwise, the person will be termed as criminal and will be allotted a jail. Court and jail manages the records of criminals and their crime. 

After sending the criminal to the Jail, he/she will be given a jail cell and work to do. Jail manages the meetings of criminals to his/her relatives. Jail also manages health record of inmates. The health record and monthly checkup of inmates is carried out and maintained by registered doctor. 

After completion of a criminal’s sentence, he/she will be released from his cell which is maintained and recorded by Jail.

# Working Site

https://crimerecordsmanagementsystem.herokuapp.com/





Languages and frameworks Used : 

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-3810/) [![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/3.2/releases/3.2.4/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://docs.djangoproject.com/en/3.2/releases/3.2.4/)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)]()
[![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)]()
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)]()
[![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)]()



## ScreenShots

![App Screenshot](https://i.postimg.cc/j5Bd5MKN/first.png)

![App Screenshot](https://i.postimg.cc/J7BzgCcQ/second.png)

![App Screenshot](https://i.postimg.cc/PqxtQg5Y/third.png)





## Installation

Start the project

```bash
  $ django-admin startproject dbms
```

Clone the repo or download the main repo and paste it in dbms folder

```bash
  $ git clone https://github.com/AkshatDhamale/DBMSProject
```

Create a database in PostGreSQL using PGAdmin or any other tool and connect the database in settings.py 


```Python
  DATABASES = {
    'default': {        

        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'crime_management_system',
        'USER':'admin',
        'PASSWORD':'testpassword',
        'HOST':'localhost',
        'PORT':'5433',
        'CONN_MAX_AGE': 500
        
    }
}
```
You can change the database or the SQL engine used according to your need.

Run the server on localhost 

```Python
  $ python manage.py runserver
```
## ER Diagrams 

![App Screenshot](https://i.postimg.cc/NFHvKfwT/ER-diagram.png)

![App Screenshot](https://i.postimg.cc/prByyDdB/Table-ER-diagram.jpg)

![App Screenshot](https://i.postimg.cc/3xqNyr3z/System-Generated-ER-Diagram.png)





## Support

For support, email akshatdhamale@gmail.com or contact me through linkedin https://www.linkedin.com/in/akshat-dhamale-444b1619b/

## Materials Used 

Template provided by: https://colorlib.com/polygon/cooladmin/index.html

Template code: https://github.com/puikinsh/CoolAdmin

Cloud application platform: Heroku - https://github.com/heroku/cli

Lucidchart: https://www.lucidchart.com/pages/

Mysql workbench: https://www.mysql.com/products/workbench/

Images used from: - https://www.pexels.com/

https://unsplash.com/

Vector icon used from : https://www.flaticon.com/

Crime management system references : https://www.grin.com/document/491032
