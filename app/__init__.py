from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_name = 'matcher.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

from app import models
from app import views

db.create_all()

# eng = create_engine(f'sqlite:///{db_name}', echo=True)
# meta = MetaData()
# meta.create_all(eng)
