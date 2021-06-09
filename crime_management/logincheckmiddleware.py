from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

class logincheckmiddleware(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == '1':
                if modulename == "crime_management.PersonViews": 
                    pass
                elif modulename == "crime_management.views" or modulename == "django.views.static" :
                    pass
                else:
                    return HttpResponseRedirect(reverse("person_home"))
            elif user.user_type == '2':
                if modulename == "crime_management.PoliceViews":
                    pass
                elif modulename == "crime_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("police_home"))
            elif user.user_type == '3':
                if modulename == "crime_management.AdminViews":
                    pass
                elif modulename == "crime_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == '4':
                if modulename == "crime_management.CourtViews":
                    pass
                elif modulename == "crime_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("court_home"))
            elif user.user_type == '5':
                if modulename == "crime_management.JailViews":
                    pass
                elif modulename == "crime_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("jail_home"))
            elif user.user_type == '6':
                if modulename == "crime_management.DoctorViews":
                    pass
                elif modulename == "crime_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("doctor_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))
        else:
            if (request.path == reverse("show_login")) or (request.path == reverse("dologin")) or (request.path == reverse("Register")):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))
