from flask import Flask, render_template, send_file, request
import os
from datetime import datetime
import pytz

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

def heure_benin():
    tz = pytz.timezone('Africa/Porto-Novo')
    return datetime.now(tz).hour

@app.before_request
def check_horaires():
    h = heure_benin()
    # Si c'est un ping cron-job.org, on le rejette la nuit
    if 'cron-job.org' in request.headers.get('User-Agent', ''):
        if h < 8:
            return 'SLEEP', 503  # Render verra une erreur et mettra en veille

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logo.svg')
def logo():
    return send_file(os.path.join(BASE, 'logo.svg'), mimetype='image/svg+xml')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
