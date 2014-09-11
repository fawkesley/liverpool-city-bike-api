#!/usr/bin/env python

import json
import logging

from citybikescraper import get_latest_locations


def main():
    logging.basicConfig(level=logging.INFO)

    locations = get_latest_locations()
    output_json = json.dumps({
        'lastRefreshed': '2014-09-11T17:38:00Z',
        'lastChanged': '2014-09-11T17:38:00Z',
        'locations': locations
    }, indent=4)

    print(output_json)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
