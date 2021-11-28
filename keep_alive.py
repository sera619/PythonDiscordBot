from flask import Flask
from threading import Thread

# simpler webserver zum aktiv halten des bots



app = Flask('')

user_id: str


@app.route('/')
@app.route('/index')
def home():
    return'''
<!DOCTYPE html>

<header>
  <nav class="navbar">
  </nav>
</header>
<body>
  <center>
    <div class="block">
      <h1>
        Python Discord-Bot © S3R43o3
      </h1>
      <p>Bot ist vollständig initialsiert.</p>
    </div>
    
    <div class="container">
      <!--
      <ul>
        <li>Bot-Name: </li>
        <li>Bot-ID: </li>
        <li>Bot-Server: </li>
      </ul>
      -->
    </div>
  </center>
</body>
<footer>

</footer>

</html>'''


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
