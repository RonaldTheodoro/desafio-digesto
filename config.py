from pathlib import Path

from decouple import Csv, config


class Config:
    """Project configurations"""
    BASE_DIR = Path(__file__).resolve().parent
    SITES = {
        'DIGITALOCEAN': config('DIGITALOCEAN'),
        'VULTR': config('VULTR'),
        'PACKET': {
            'TINY': config('PACKET_TINY'),
            'COMPUTE': config('PACKET_COMPUTE'),
            'MEMORY': config('PACKET_MEMORY'),
            'STORAGE': config('PACKET_STORAGE'),
            'ACCELERATOR': config('PACKET_ACCELERATOR'),
        },
    }
