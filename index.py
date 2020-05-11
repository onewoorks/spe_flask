from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS, cross_origin
from app.main.controllers import api

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)
app.run(debug=True,host="0.0.0.0") 