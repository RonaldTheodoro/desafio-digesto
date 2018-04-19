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
