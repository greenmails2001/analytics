#templatetags.py
from testapp.models import VehicleBrand
from django import template

register = template.Library()

@register.inclusion_tag("brand_model_select.html")
def brand_model_select():
    brand_list = VehicleBrand.objects.all()
    return {'brand_list' : brand_list}