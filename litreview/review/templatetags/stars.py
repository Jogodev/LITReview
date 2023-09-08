from django import template

register = template.Library()


@register.filter(name='stars')
def stars(number, max_stars=5):
    """Tranform a number to stars"""
    if number > max_stars:
        return "★" * max_stars
    elif number < 1:
        return "☆" * max_stars
    return "★" * number + "☆" * (max_stars - number)
