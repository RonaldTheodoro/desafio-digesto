from argparse import ArgumentParser

from dispatcher import Dispatcher


if __name__ == '__main__':
    parser = ArgumentParser(
        description='A simple tool for get the price from cloud services'
    )
    parser.add_argument(
        '-s',
        '--services',
        default='all',
        choices=['vultr', 'digitalocean'],
        help='Choice an individual service to get the data'
    )
    args = parser.parse_args()
    dispatcher = Dispatcher(args.services)
