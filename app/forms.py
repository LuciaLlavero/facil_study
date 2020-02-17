from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

class SummaryForm(FlaskForm):
	text = TextAreaField()
	summarize = SubmitField("Summarize")