from flask import Flask, jsonify,request


from dotenv import load_dotenv
import os
from views.Account import Account


load_dotenv()
app = Flask(__name__)






app.add_url_rule('/account/', view_func = Account.as_view('acc'))
# app.add_url_rule('/image/',view_func = Image.as_view('image'))