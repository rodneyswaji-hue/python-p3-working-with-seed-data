import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game

engine = create_engine('sqlite:///games.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

print("Starting ipdb shell. Access `session` to query the database.")
ipdb.set_trace()