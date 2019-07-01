from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

#replace .0 by space
@register.filter
def pointzero(value):
    return value.replace(".0","")

#replace 1 and 2 by Yes and No
@register.filter
@stringfilter
def yesno(value):
    if value == '1.0':
        value = 'Yes'        
    elif value == '2.0':
        value = 'No'
    return value

#replace 1,2,3 by High, Medium,Low for scale of impact
@register.filter
@stringfilter
def hml(value):
    if value == '1.0':
        value = 'High'        
    elif value == '2.0':
        value = 'Medium'
    elif value == '3.0':
        value = 'Low'
    return value


#replace 1,2,3,4 for repair status
@register.filter
@stringfilter
def rs(value):
    if value == '1.0':
        value = 'No need to repair'        
    elif value == '2.0':
        value = 'Need minor repair'
    elif value == '3.0':
        value = 'Need major repair'
    elif value == '3.0':
        value = 'Repair not possible'
    return value
