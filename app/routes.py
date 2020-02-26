from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SummaryForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index() : 
	form = SummaryForm()
	if form.validate_on_submit() :
		return redirect(url_for('summary'))
	return render_template('index.html', form=form)

@app.route('/summary')
def summary() :
	print('test')
	return render_template('summary.html')	