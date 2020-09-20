from flask import render_template
from app import app, W, SchemeList


@app.route('/')
@app.route('/index')
def index():
    # user = {'username': app.Scheme("name", 7, 0, 15, 0)}
    weekdays = {'weekdays': W}
    for day in weekdays['weekdays']:
        print(type(day))
    return render_template('index.html', title='Home', weekdays=weekdays,
                           schemes=SchemeList)
