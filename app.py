from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()  # Ton HTML principal

@app.route('/get_ip')
def get_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({'ip': ip})

if __name__ == '__main__':
    app.run(debug=True)
