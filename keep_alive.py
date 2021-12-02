from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from main import server_id, server_name, bot_id, bot_name, server_id
from threading import Thread


# simpler webserver zum aktiv halten des bots
app = Flask('')
Bootstrap(app)
app.config['SECRET_KEY'] = 'KANI'
# Flask-Bootstrap need this

user_id: str
FARBEN = ['blau', 'rot', 'grün', 'gelb']


# -> name Form
class NameForm(FlaskForm):
  name = StringField('Welche Farbe ist deine Lieblingsfarbe?',
                     validators=[DataRequired()])
  submit = SubmitField('Abschicken')


@app.route('/')
def home():
	return render_template('index.html', server_id=server_id, bot_id=bot_id, server_name=server_name)

def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
