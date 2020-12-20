from flask import Flask
from flask_cors import CORS

import waitress

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


import social_media
app.register_blueprint(social_media.blueprint)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    waitress.serve(app,host='0.0.0.0', port=5400)
