from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

from .models import Base, Machine


engine = create_engine(Config.DATABASE, echo=True)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()


def save_machine(machine):
    session.add(machine)
    session.commit()


def save_machine_bulk(machine):
    session.bulk_save_objects(machine)
    session.commit()


def get_all_machines():
    return session.query(Machine).all()