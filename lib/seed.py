import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Game

# Connect to the SQLite database (create if doesn't exist)
engine = create_engine('sqlite:///games.db', echo=False)

# Create tables if they don't exist (optional if using Alembic)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

print("Seeding games...")

# Delete existing data to avoid duplicates on reseed
session.query(Game).delete()
session.commit()

# Generate 50 fake game records
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

session.bulk_save_objects(games)
session.commit()

print("Seed complete!")