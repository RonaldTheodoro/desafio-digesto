import re

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import Config


Base = declarative_base()


class Machine(Base):
    __tablename__ = 'machine'
    id = Column('id', Integer, primary_key=True)
    site = Column('site', String(50))
    name = Column('name', String(50))
    cpus = Column('cpus', String(50))
    memory = Column('memory', String(50))
    storage = Column('storage', String(50))
    bandwidth = Column('bandwidth', String(50))
    price_month = Column('price_month', String(50))
    price_hour = Column('price_hour', String(50))

    def __init__(self, site='', name='', cpus='', memory='', storage='', bandwidth='', price_month='', price_hour=''):
        self.site = self.clean_field(site)
        self.name = self.clean_field(name)
        self.cpus = self.clean_field(cpus)
        self.memory = self.clean_field(memory)
        self.storage = self.clean_field(storage)
        self.bandwidth = self.clean_field(bandwidth)
        self.price_month = self.clean_field(price_month)
        self.price_hour = self.clean_field(price_hour)

    def show_machine_info(self):
        print(f'site: {self.site}')
        print(f'name: {self.name}')
        print(f'cpus: {self.cpus}')
        print(f'memory: {self.memory}')
        print(f'storage: {self.storage}')
        print(f'bandwidth: {self.bandwidth}')
        print(f'price_month: {self.price_month}')
        print(f'price_hour: {self.price_hour}')

    def clean_field(self, field):
        """Remove whitespaces"""
        return re.sub(r'\s+', ' ', field).strip()



engine = create_engine(Config.DATABASE, echo=True)
Base.metadata.create_all(bind=engine)
