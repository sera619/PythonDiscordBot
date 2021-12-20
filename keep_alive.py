from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import  SubmitField, FormField, validators, StringField
from wtforms.validators import DataRequired
from threading import Thread

# simpler webserver zum aktiv halten des bots




app = Flask('')
app.config['SECRET_KEY'] = 'KANI'
# Flask-Bootstrap need this
Bootstrap(app)


# -> name Form
class NameForm(FlaskForm):
    title = StringField('Gebe den Titel ein: ', validators=[DataRequired()])
    submit = SubmitField('Abschicken')

class TextField(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Abschicken')

class InfoForm(FlaskForm):
    panel = FormField()

class NavItem(FlaskForm):
    submit = SubmitField('Home')

name_bot = ""
name_server = "" 
id_bot =""
id_server =""
bot_status =""
bot_version =""
count_member = ""

text_title = ""

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html', bot_version=bot_version)

@app.route('/stats', methods=('GET','POST'))
def stats():
    return render_template('stats.html',server_name= name_server, server_id = id_server, bot_name = name_bot, bot_id = id_bot, bot_status=bot_status ,bot_version=bot_version)


@app.route('/commands', methods=('GET','POST'))
def coms():
    return render_template('test.html')



@app.route('/options', methods=['POST','GET'])
def options():
    return render_template('options.html', )

titles = ['title1', 'title2', 'title3']


@app.route('/debugging', methods=['POST', 'GET'])
def debug():      
    form = NameForm()
    title = "OPTIONEN"
    message = "Seite funktioniert"
    # get text from input
    if form.validate_on_submit():
        title_text = form.title.data
        text_title = title_text
        return render_template('debugging.html', form = form, title=title, message = text_title)
    return render_template('debugging.html', form =form, title= title, message = message)



def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
