from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import  SubmitField, FormField
from wtforms.validators import DataRequired
import discord
from discord.embeds import Embed as EM
from threading import Thread

# simpler webserver zum aktiv halten des bots




app = Flask('')
app.config['SECRET_KEY'] = 'KANI'
# Flask-Bootstrap need this
Bootstrap(app)


# -> name Form
class NameForm(FlaskForm):
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
    return render_template('options.html')

def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
