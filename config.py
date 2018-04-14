from pathlib import Path

from decouple import Csv, config


class Config:
    """Project configurations"""
    BASE_DIR = Path(__file__).resolve().parent
    SITES = {
        'DIGITALOCEAN': config('DIGITALOCEAN'),
        'VULTR': config('VULTR'),
        'PACKET': config('PACKET'),
    }
