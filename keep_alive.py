from flask import Flask
from threading import Thread
# simpler webserver zum aktiv halten des bots


app = Flask('')


@app.route('/')
def home():
    return '''
<!DOCTYPE html>

<head>
  <link rel="stylesheet" href="templates/style.css" type="text/css" />
</head>
<header>
  <nav class="navbar"></nav>
</header>

<body>
  <div class="block">
    <h1>
      Python Discord-Bot © S3R43o3
    </h1>
  </div>
  <div class="container">
    <p class="text">

    </p>
  </div>
</body>
<footer>

</footer>

</html>'''


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
