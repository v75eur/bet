from flask import Flask, render_template, send_file
import os

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logo.svg')
def logo():
    return send_file(os.path.join(BASE, 'logo.svg'), mimetype='image/svg+xml')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
