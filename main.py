#!/usr/bin/env python

from argparse import ArgumentParser

from dispatcher import Dispatcher
from models.db import Database


def parser_args():
    """Define cmd arguments"""
    parser = ArgumentParser(
        description='Uma simples ferramenta para conseguir o preço de sites de cloud service'
    )
    parser.add_argument(
        '--service',
        default='all',
        choices=['vultr', 'digitalocean'],
        help='Selecione um site em expecifico'
    )
    parser.add_argument(
        '--down',
        action='store_true',
        help='Baixar os registros'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        help='Salva os registros no banco'
    )
    parser.add_argument(
        '--show',
        action='store_true',
        help='Mostra os registros salvos'
    )
    parser.add_argument(
        '--delete',
        action='store_true',
        help='Exclui todos os registros'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parser_args()
    database = Database()
    machines = []

    if args.down:
        dispatcher = Dispatcher(args.service)
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