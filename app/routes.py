from flask import render_template
from app import app, W, SchemeList


@app.route('/')
@app.route('/index')
def index():
    weekdays = {'weekdays': W}
    return render_template('index.html', title='Home', weekdays=weekdays,
                           schemes=SchemeList)


@app.route('/schemes/<scheme>')
def scheme(scheme):
    for ischeme in SchemeList:
        if scheme == ischeme.name:
            return str(ischeme)
    return str(SchemeList)


