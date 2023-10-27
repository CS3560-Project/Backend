from flask import Flask 
from dotenv import load_dotenv
load_dotenv()
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return '<h1> There!</h1>'

    return app
