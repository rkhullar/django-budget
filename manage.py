#!/usr/bin/env python
from configparser import RawConfigParser
from pathlib import Path
import sys
import os


def iter_config(path: Path):

    if path.exists():
        config = RawConfigParser()
        with path.open('r') as f:
            config.read_file(f)

        for section in config.sections():
            for key, val in config[section].items():
                yield key, val


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nyit.settings')
    to_read = Path(__file__).parent / 'local' / 'config.cfg'
    for key, val in iter_config(to_read):
        os.environ.setdefault(key.upper(), val)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
