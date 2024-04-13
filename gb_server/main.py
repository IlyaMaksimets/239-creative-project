from flask import Flask
from flask_cors import CORS
from app_routes import simple_page
from models import db

app = Flask(__name__, static_folder="build", static_url_path='')
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
CORS(app, supports_credentials=True)
app.register_blueprint(simple_page, url_prefix='/cp_api')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
