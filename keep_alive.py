from flask import Flask
from threading import Thread
from main import main
# simpler webserver zum aktiv halten des bots


app = Flask('')


@app.route('/')
def home():
    return '''
<!DOCTYPE html>

<header>
  <nav class="navbar"></nav>
</header>

<body>
  <center>
    <div class="block">
      <h1>
        Python Discord-Bot © S3R43o3
      </h1>
    </div>
    
    <div class="container">
      <ul>
        <li>Bot-Name: {main.user.name}</li>
        <li>Bot-ID: {main.user.id}</li>
        <li>Bot-Server: {main.guild.name}</li>
      </ul>
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
