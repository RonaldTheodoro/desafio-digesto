from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

from .models import Base, Machine


class Database:
    """Handle the database access"""
    engine = create_engine(Config.DATABASE, echo=False)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    def save_machine_bulk(self, machine):
        """Save all machines"""
        self.session.bulk_save_objects(machine)
        self.session.commit()

    def get_all_machines(self):
        """Get all registers from db"""
        return self.session.query(Machine).all()

    def delete_all(self):
        """Delete all registers"""
        rows = 0
        try:
            rows = self.session.query(Machine).delete()
            self.session.commit()
        except:
            self.session.rollback()
        return rows
