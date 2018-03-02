import calendar

from app import app


@app.template_filter('to_day')
def to_day(n):
    return calendar.day_name[(n-1) % 7]

