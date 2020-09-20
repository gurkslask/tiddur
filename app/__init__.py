from flask import Flask

from app.time_cmd.scheme import Scheme
from app.time_cmd.week import Week
S = Scheme("Work", 7, 0, 16, 4)
SchemeList = [S]
W = Week()
W.addmonday(S)
app = Flask(__name__)

from app import routes
