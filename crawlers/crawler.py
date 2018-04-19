from abc import ABC, abstractmethod
from collections import namedtuple

import requests

from bs4 import BeautifulSoup


class Crawler(ABC):
    """Get html from site"""
    site = None
    html = None

    def __init__(self, url):
        self.get_response(url)
        self.get_html()

    def get_response(self, url):
        """Get http response from server"""
        self.response = requests.get(url)

    def get_html(self):
        """Get the html page"""
        if self.response.status_code == 200:
            self.parser_html()
        else:
            self.raise_error()

    def parser_html(self):
        """Parser the html"""
        self.html = BeautifulSoup(self.response.text, "html.parser")

    def raise_error(self):
        """Raise an error if couldn't reach the page"""
        status_code = self.response.status_code
        reason = self.response.reason
        raise Exception(f'Status code: {status_code} Reason: {reason}')

    def get_machine_obj(self, name='', cpus='', memory='', storage='', bandwidth='', price_month='', price_hour=''):
        """Create and return a machine instance"""
        machine = Machine(
            site=self.site,
            name=name,
            cpus=cpus,
            memory=memory,
            storage=storage,
            bandwidth=bandwidth,
            price_month=price_month,
            price_hour=price_hour
        )
        return machine

    @abstractmethod
    def get_info(self):
        """Get info from html, must be implement by the sub class"""
        pass


class Machine:

    def __init__(self, site='', name='', cpus='', memory='', storage='', bandwidth='', price_month='', price_hour=''):
        self.site = site
        self.name = name
        self.cpus = cpus
        self.memory = memory
        self.storage = storage
        self.bandwidth = bandwidth
        self.price_month = price_month
        self.price_hour = price_hour

    def __str__(self):
        return f'{self.site} - {self.name}'

    def show_machine_info(self):
        print('site', self.site)
        print('name', self.name)
        print('cpus', self.cpus)
        print('memory', self.memory)
        print('storage', self.storage)
        print('bandwidth', self.bandwidth)
        print('price_month', self.price_month)
        print('price_hour', self.price_hour)
