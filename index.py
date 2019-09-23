from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from app.main.controllers import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)
app.run(debug=True,host="0.0.0.0") 