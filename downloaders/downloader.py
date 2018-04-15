from abc import ABC, abstractmethod
from collections import namedtuple

import requests

from bs4 import BeautifulSoup


class Downloader(ABC):
    """Get html from site"""
    site = None
    html = None

    def __init__(self, url):
        self.get_response(url)
        self.get_html()

    def get_response(self, url):
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

    def get_machine_obj(self, name, cpus, memory, storage, bandwidth, price_month, price_hour):
        return Machine(
            site=self.site,
            name=name,
            cpus=cpus,
            memory=memory,
            storage=storage,
            bandwidth=bandwidth,
            price_month=price_month,
            price_hour=price_hour
        )

    @abstractmethod
    def get_info(self):
        """Get info from html, must be implement by the sub class"""
        pass


Machine = namedtuple('Machine', [
    'site',
    'name',
    'cpus',
    'memory',
    'storage',
    'bandwidth',
    'price_month',
    'price_hour'
])
