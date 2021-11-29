from flask import Flask
from flask import render_template
from threading import Thread

# simpler webserver zum aktiv halten des bots



app = Flask('')

user_id: str


@app.route('/')
def home():
    return'''
<!DOCTYPE html>

<head>
  <meta charset="utf-8">
  <title>Python Discord-Bot by © S3R43o3</title>
  <style>
    html{
      background-color: rgb(182, 214, 214);
      color: darkred;
    }
    .color {
      width:80%;
      border: 1px solid black;
      margin: 5;
      display: block;
      font-style: bold;
      font-size: xxl;
    }
  </style>
  <script src="https://kit.fontawesome.com/c158cba94c.js" crossorigin="anonymous"></script>
</head>

<header>
  <nav class="navbar">
  </nav>
</header>
<body>
  <center>
    <div class="color">
      <h1><i class="fa-brands fab-python</i><i class="fa-brands fab-discord"></i></h1>
        <h1>Python Discord-Bot © S3R43o3
      </h1>
      <h2><i class="fa fa-broadcast-tower></i></h2>
      <p>Bot ist vollständig initialsiert.</p>      
        <h2><i class="fa fa-braille></i>Bot Informationen:</h2>
    </div>
    <div>
    <!--
      <ul>
        <li>Bot-Name: </li>
        <li>Bot-ID: </li>
        <li>Bot-Server: </li>
      </ul>-->
    </div>
  </center>
</body>
<footer>

</footer>

</html>'''

@app.route('/index')
def index():
  return render_template()

def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
