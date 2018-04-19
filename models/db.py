from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

from .models import Base, Machine


class Database:
    engine = create_engine(Config.DATABASE, echo=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    def save_machine_bulk(self, machine):
        self.session.bulk_save_objects(machine)
        self.session.commit()

    def get_all_machines(self):
        return self.session.query(Machine).all()
