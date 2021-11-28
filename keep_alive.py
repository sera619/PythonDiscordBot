from flask import Flask
from threading import Thread

# simpler webserver zum aktiv halten des bots
user_id = 'user id'
user_name = 'user name'
server_name = 'server name'
app = Flask('')



def change_bot_stats(servername, userid, username):
  user_id = userid
  user_name = username
  server_name = servername

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
        <li>Bot-Name: {user_name}</li>
        <li>Bot-ID: {user_id}</li>
        <li>Bot-Server: {server_name}</li>
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
