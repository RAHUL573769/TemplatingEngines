from django import template
from django.template.loader import get_template

register = template.Library()


def my_template(value, args):
    if args == "change":
        value = "Rahim"
        return value


def show_courses():
    courses: [
        {"id": 1, "courses": " c", "teaher": "Abdul"},
        {"id": 2, "courses": " c++", "teaher": "Abdul"},
    ]
    return courses


register.filter("change_name", my_template)
course_template = get_template("firstapp/courses.html")
register.inclusion_tag(course_template)(show_courses)
