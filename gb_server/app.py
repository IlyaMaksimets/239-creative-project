from flask import Flask
from flask_cors import CORS
from app_routes import simple_page

app = Flask(__name__)
app.config['SESSION_COOKIE_HTTPONLY'] = False
CORS(app, supports_credentials=True)
app.register_blueprint(simple_page)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == '__main__':
    app.run()
