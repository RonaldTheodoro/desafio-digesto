from .crawler import Crawler, Machine


class VultrPriceTable(Crawler):
    """Get price info from Vultr"""
    site = 'VULTR'

    def get_info(self):
        elements = self.html.find_all('a', {'class': 'package'})
        return list(map(self.get_machine, elements))

    def get_machine(self, element):
        """Get one machine"""
        header = element.find('div', {'class': 'package-header'})
        body = element.find('div', {'class': 'package-body'})
        items = body.ul.find_all('li')

        storage = header.h3.text
        price_hour = header.span.attrs['data-hourly']
        price_month = header.span.attrs['data-monthly']
        cpus = items[0].text
        memory = items[1].text
        bandwidth = items[2].text

        return self.get_machine_obj(
            storage,
            cpus,
            memory,
            storage,
            bandwidth,
            price_month,
            price_hour
        )
