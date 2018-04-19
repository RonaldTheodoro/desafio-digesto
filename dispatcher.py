from itertools import chain

import downloaders
from config import Config


class Dispatcher:
    factories = []

    def __init__(self, services):
        self.select_services(services)
        for machine in self.get_machines():
            print(machine.show_machine_info())

    def select_services(self, services):
        if services == 'all':
            self.add_instance(self.vultr_factory(Config.SITES['VULTR']))
            self.add_instance(
                self.digitalocean_factory(Config.SITES['DIGITALOCEAN'])
            )
        elif services == 'vultr':
            self.add_instance(self.vultr_factory(Config.SITES['VULTR']))
        elif services == 'digitalocean':
            self.add_instance(
                self.digitalocean_factory(Config.SITES['DIGITALOCEAN'])
            )

    def add_instance(self, instance):
        """Add a instance in factories list"""
        self.factories.append(instance)

    def get_machines(self):
        """Get a list with all machines"""
        return list(chain.from_iterable(map(self.get_info, self.factories)))

    def get_info(self, factory):
        """Call the get_info method from factory instance"""
        return factory.get_info()

    def vultr_factory(self, url):
        """Return an VultrPriceTable instance"""
        return downloaders.VultrPriceTable(url)

    def digitalocean_factory(self, url):
        """Return an DigitalOceanPriceTable instance"""
        return downloaders.DigitalOceanPriceTable(url)
