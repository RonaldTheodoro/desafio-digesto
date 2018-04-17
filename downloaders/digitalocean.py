import re

from .downloader import Downloader, Machine


class DigitalOceanPriceTable(Downloader):
    """Get price info from DigitalOcean"""
    site = 'DIGITALOCEAN'

    def get_info(self):
        elements = self.html.find(
            'div',
            {'class': 'bui-GridContainer bui-GridContainer-largeGutter@medium'}
        )
        titles = elements.find_all('h2')
        tables = elements.find_all(
            'table',
            {'class': 'bui-Table PricingTable'}
        )
        machines = []
        for title, table in zip(titles, tables):
            machines += self.create_table(title, table)
        return machines

    def create_table(self, title, table):
        rows = table.tbody.find_all('tr')
        tables = map(self.create_row, rows)
        machines = []
        for table in tables:
            table.name = title.text
            machines.append(table)
        return machines

    def create_row(self, row):
        line_elements = row.find_all('td')
        machine = self.get_price(line_elements[4].text)
        machine.site = self.site
        machine.memory = line_elements[0].text
        machine.cpus = line_elements[1].text
        machine.storage = line_elements[2].text
        machine.bandwidth = line_elements[3].text
        return machine

    def get_price(self, price):
        m = re.search(r'\$(\d+)/mo  \$(\d\.\d+)/hr', price)
        price_month, price_hour = m.groups()
        machine = Machine()
        machine.price_month = price_month
        machine.price_hour = price_hour
        return machine
