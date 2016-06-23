from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
  
class Search_Records_Form(Form):
    event_id = StringField('event_id', validators=[DataRequired()])
