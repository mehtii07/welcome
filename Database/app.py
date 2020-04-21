import os
from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mahtab'
#############################
###       Database        ###
#############################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
#############################
###       Models          ###
#############################


class name1(db.Model):
  __tablename__ = 'practice'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  age = db.Column(db.Integer)

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"User name is {self.name} and age is {self.age}"


#####################################
###       View FUNCTIONS          ###
#####################################


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
  form = AddForm()
  if form.validate_on_submit():
    name = form.data.name
    age = form.data.age
    new_name = name1(name)
    new_age = name1(age)
    db.session.add(new_name)
    db.session.add(new_age)
    de.session.commit()

    return redirect(url_for('listuser'))

  return render_template('add.html', form=form)


@app.route('/listuser')
def listuser():
  user = name1.query.all()
  return render_template('listuser.html', user=user)


@app.route('/dele')
def dele():
  form = DelForm()
  if form.validate_on_submit():
    id = form.id.data
    user = name1.query.get(id)
    de.session.delete(user)
    db.session.commit()
    return redirect(url_for('listuser'))
  return render_template('dele.html')


if __name__ == '__main__':
  app.run(debug=True)
