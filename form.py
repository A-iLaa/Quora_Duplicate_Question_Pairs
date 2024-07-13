from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

from wtforms.validators import DataRequired

class PredictForm(FlaskForm):
    q1=StringField("Enter Question 1",validators=[DataRequired()])
    q2=StringField("Enter Question 2",validators=[DataRequired()])
    submit =SubmitField("Predict")