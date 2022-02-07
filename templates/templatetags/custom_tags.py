from django.template.defaulttags import register


@register.filter
def add_css(field, css):
    return field.as_widget(attrs={"class": css})
