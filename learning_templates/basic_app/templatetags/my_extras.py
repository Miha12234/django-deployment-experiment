from  django import template

register = template.Library()

#way 2
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')


#way 1
# register.filter('cut',cut)
