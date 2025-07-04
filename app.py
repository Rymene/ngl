from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ngl.html')


@app.route('/get_ip')
def get_ip():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    timestamp = datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S')  # Format : 2025-07-04 14:23:10

    # Écriture dans le fichier texte
    with open('ips.txt', 'a') as f:
        f.write(f'{timestamp} - {ip_address}\n')

    return jsonify({'ip': ip_address})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
