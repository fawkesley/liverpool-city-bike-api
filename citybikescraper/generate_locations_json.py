#!/usr/bin/env python

import datetime
import json
import pytz

from .get_latest_locations import get_latest_locations


def generate_locations_json():
    locations = get_latest_locations()
    output_json = json.dumps({
        'lastRefreshed': format_datetime(utc_now()),
        'locations': locations
    }, indent=4)

    return output_json


def format_datetime(dt):
    assert dt.tzinfo == pytz.UTC
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def utc_now():
    return datetime.datetime.now(pytz.UTC)
