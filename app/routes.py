from flask import render_template
from app import app
from datetime import datetime
from pytz import timezone
import getpass
from app.forms import SummaryForm

@app.route('/')
@app.route('/index')
def index() :
	return render_template('index.html', user=getpass.getuser(), local_datetime=datetime.now(timezone('UTC')), form=SummaryForm())