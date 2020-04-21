# from flask import Flask, render_template, redirect, url_for,session
# from flask_wtf import FlaskForm
# from wtforms import (StringField, SubmitField, TextAreaField,
#                      TextField, BooleanField, RadioField, PasswordField, SelectField,)
# from wtforms.validators import DataRequired

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'Mahtab'


# class Info(FlaskForm):
#     name = StringField('Enter your name', validators=[DataRequired()])
#     email = StringField('Enter your email', validators=[DataRequired()])
#     password = PasswordField('Enter your password',
#                              validators=[DataRequired()])
#     foodchoice = SelectField('Select ur food choice', choices=[
#                              ('1', 'Veg'), ('2', 'Non-Veg')])
#     room_c = RadioField('Select ur Room', choices=[
#                         ('1', 'AC'), ('2', 'Non-Ac')])
#     submit = SubmitField()


# @app.route('/', methods=['GET', 'POST'])
# def index():
#   form = Info()
#   if form.validate_on_submit():
#     session['name'] = form.name.data
#     return redirect(url_for('thankyou'))
    

#   return render_template('index.html', form=form)


# @app.route('/thankyou')
# def thankyou():
#   return render_template('thankyou.html')




# if __name__ == "__main__":
#   app.run(debug=True)
import  os

print(os.path.abspath(os.path.dirname(__file__)))