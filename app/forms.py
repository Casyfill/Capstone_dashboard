from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class Add_Records_Form(Form):
    crimeId = StringField('crimeId', validators=[DataRequired()])
    modeOfEntry = StringField('modeOfEntry', validators=[DataRequired()])
