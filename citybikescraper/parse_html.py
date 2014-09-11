import json
import re


def parse_html(f):
    match = re.search(
        'var mapDataLocations = (?P<locations>\[{.*}\]);',
        f.read())
    if match is not None:
        return reformat(json.loads(match.group('locations')))
    else:
        raise ValueError("Failed to parse.")


def reformat(locations):
    for location in locations:
        yield {
            'latitude': float(location['Latitude']),
            'longitude': float(location['Longitude']),
            'locationName': location['LocalTitle'].strip(),
            'availableBikes': int(location['AvailableBikesCount']),
            'availableLocks': int(location['FreeLocksCount'])
            }
