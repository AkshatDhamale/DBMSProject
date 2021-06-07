from django import template
from crime_management.models import Police
register = template.Library()

@register.simple_tag
def show_pending_reports(user):
    pol=Police.objects.get(admin_id=user.id)
    pol_image=pol.officer_image
    return pol_image

