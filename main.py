#!/usr/bin/env python

from argparse import ArgumentParser

from dispatcher import Dispatcher
from models.db import Database


def parser_args():
    """Define cmd arguments"""
    parser = ArgumentParser(
        description='A simple tool for get the price from cloud services'
    )
    parser.add_argument(
        '--service',
        default='all',
        choices=['vultr', 'digitalocean'],
        help='Choice an individual service to get the data'
    )
    parser.add_argument(
        '--down',
        action='store_true',
        help='Download registers'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        help='Save registers in database'
    )
    parser.add_argument(
        '--show',
        action='store_true',
        help='Show registers in database'
    )
    parser.add_argument(
        '--delete',
        action='store_true',
        help='Delete all registers in database'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parser_args()
    database = Database()
    machines = []

    if args.down:
        dispatcher = Dispatcher(args.services)
        machines = dispatcher.get_machines()

    if args.save:
        database.save_machine_bulk(machines)

    if args.show:
        machines = database.get_all_machines()
        for machine in machines:
            print(machine.show_machine_info())

    if args.delete:
        rows = database.delete_all()
        print(f'{rows} rows deleted')