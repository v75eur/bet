from flask import Flask, render_template, send_file, request
import os
from datetime import datetime
import pytz

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

def heure_benin():
    tz = pytz.timezone('Africa/Porto-Novo')
    return datetime.now(tz).hour

@app.route('/health')
def health():
    # TOUJOURS 200 - sinon Render endort le service
    h = heure_benin()
    status = "OK - Ouvert" if h >= 8 else "PAUSE - Reprise 8H Benin"
    return status, 200

@app.route('/')
def index():
    h = heure_benin()
    if h < 8:
        return '<h2 style="text-align:center;margin-top:50px">🔴 BETPOWO ouvre à 8H Bénin</h2>', 503
    return render_template('index.html')

@app.route('/logo.svg')
def logo():
    return send_file(os.path.join(BASE, 'logo.svg'), mimetype='image/svg+xml')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
