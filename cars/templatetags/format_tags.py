from django import template

register = template.Library()

@register.filter
def brl(value):
    try:
        value = float(value)
        return f'R$ {value:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')
    except (ValueError, TypeError):
        return value
