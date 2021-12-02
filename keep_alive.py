from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from main import server_id, server_name, bot_id, bot_name
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
    
	return render_template('index.html')
# ------> Alte Home-Seite
#
#
# def home():
#     return'''
# <!DOCTYPE html>

# <head>
#   <meta charset="utf-8">
#   <title>Python Discord-Bot by © S3R43o3</title>
#   <style>
#     html{
#       background-color: rgb(182, 214, 214);
#       color: darkred;
#     }
#     .color {
#       width:80%;
#       border: 1px solid black;
#       margin: 5;
#       display: block;
#       font-style: bold;
#       font-size: xxl;
#     }
#   </style>
#   <script src="https://kit.fontawesome.com/c158cba94c.js" crossorigin="anonymous"></script>
# </head>


# <body>
#   <center>
#     <div class="color">
#       <nav class="navbar">
#       <a href="#">Home</a>
#       </nav>

#       <h1>
#         <i class="fa-brands fab-python"></i>
#         <i class="fa-brands fab-discord"></i>
#       </h1>
#       <h1>
#         Python Discord-Bot © S3R43o3
#       </h1>
#       <h2><i class="fa fa-broadcast-tower></i></h2>
#       <p>Bot ist vollständig initialsiert.</p>
#         <h2><i class="fas fa-braille></i>Bot Informationen:</h2>
#     </div>
#     <div>
#     <!--
#       <ul>
#         <li>Bot-Name: </li>
#         <li>Bot-ID: </li>
#         <li>Bot-Server: </li>
#       </ul>-->
#     </div>
#   </center>
# </body>
# <footer>

# </footer>

# </html>'''


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
