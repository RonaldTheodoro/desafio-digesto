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
        """Get rows from html tables"""
        rows = table.tbody.find_all('tr')
        tables = map(self.create_row, rows)
        machines = []
        for table in tables:
            table.name = title.text
            machines.append(table)
        return machines

    def create_row(self, row):
        """Get all infos from html and return a object"""
        line_elements = row.find_all('td')
        memory = line_elements[0].text
        cpus = line_elements[1].text
        storage = line_elements[2].text
        bandwidth = line_elements[3].text
        price_month, price_hour = self.get_price(line_elements[4].text)
        return self.get_machine_obj(
            memory=memory,
            cpus=cpus,
            storage=storage,
            bandwidth=bandwidth,
            price_month=price_month,
            price_hour=price_hour
        )

    def get_price(self, price):
        """Get the price using regex"""
        m = re.search(r'\$(\d+)/mo  \$(\d\.\d+)/hr', price)
        return m.groups()
