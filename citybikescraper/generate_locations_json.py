#!/usr/bin/env python

import json

from .get_latest_locations import get_latest_locations


def generate_locations_json():
    locations = get_latest_locations()
    output_json = json.dumps({
        'lastRefreshed': '2014-09-11T17:38:00Z',
        'lastChanged': '2014-09-11T17:38:00Z',
        'locations': locations
    }, indent=4)

    return output_json
