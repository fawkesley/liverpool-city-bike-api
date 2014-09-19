#!/usr/bin/env python

import logging

from citybikescraper import generate_locations_json, upload_locations_json


def main():
    logging.basicConfig(level=logging.INFO)

    json_string = generate_locations_json()
    upload_locations_json(json_string)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
