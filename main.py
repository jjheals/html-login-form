from flask import Flask
from flask import render_template, request
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
from auth import *

app = Flask(__name__)

compress = Compress()
compress.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', errorStatus='hidden')


@app.route('/login', methods=['POST'])
def login():
    
    print(f'given username: {request.form.get("username")}')
    print(f'given password: {request.form.get("password")}')

    if authenticate(request.form.get('username'), request.form.get('password')):
        return render_template('dash.html')
    else: return render_template('index.html', errorStatus = 'flex')
    





if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()