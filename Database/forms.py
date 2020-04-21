from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField,validators
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
  name = StringField('Enter your name')
  age = IntegerField('Enter Your age')
  submit = SubmitField("Add User")


class DelForm(FlaskForm):
  id = IntegerField('Enter Id number to remove')
  submit = SubmitField("Remove User")
