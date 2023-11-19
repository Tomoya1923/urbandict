from flask import Flask
app = Flask(__name__)
import urbandict.app

from urbandict import db
db.create_dictionary_table()