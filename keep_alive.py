from flask import Flask
from threading import Thread
#simpler webserver zum aktiv halten des bots

app = Flask('')


@app.route('/')
def home():
    return render_template('index.html')


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
