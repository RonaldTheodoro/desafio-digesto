from abc import ABC, abstractmethod
from collections import namedtuple

import requests

from bs4 import BeautifulSoup
from config import Config


class Downloader(ABC):
    site = None
    html = None

    def __init__(self):
        self.response = requests.get(Config.SITES[self.site])
        self.get_html()

    def get_html(self):
        if self.response.status_code == 200:
            self.parser_html()
        else:
            self.raise_error()

    def parser_html(self):
        self.html = BeautifulSoup(self.response.text, "html.parser")

    def raise_error(self):
        status_code = self.response.status_code
        reason = self.response.reason
        raise Exception(f'Status code: {status_code} Reason: {reason}')

    @abstractmethod
    def get_info(self):
        pass


Machine = namedtuple(
    'Machine', 
    [
        'site',
        'name',
        'cpus',
        'memory',
        'storage',
        'bandwidth',
        'price_month',
        'price_hour'
    ]
)
