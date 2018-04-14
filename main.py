from downloaders import VultrPriceTable, DigitalOceanPriceTable


if __name__ == '__main__':
    vultr = VultrPriceTable()
    machines = vultr.get_info()
    for machine in machines:
        print(machine)