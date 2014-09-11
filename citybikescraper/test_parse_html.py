from __future__ import unicode_literals

from os.path import dirname, join as pjoin

from nose.tools import (assert_equal, assert_is_instance, assert_greater_equal,
                        assert_less_equal, assert_not_equal)

from .parse_html import parse_html

_HTML_FILE = pjoin(dirname(__file__), 'sample_data', 'LocationsMap.aspx')

with open(_HTML_FILE, 'r') as f:
    LOCATIONS = list(parse_html(f))


def test_that_1421_locations_are_loaded():
    assert_equal(64, len(LOCATIONS))


def test_that_every_latitude_is_floating_point():
    for latitude in (l['latitude'] for l in LOCATIONS):
        yield assert_is_instance, latitude, float


def test_that_every_longitude_is_floating_point():
    for longitude in (l['longitude'] for l in LOCATIONS):
        yield assert_is_instance, longitude, float


def test_that_every_latitude_is_reasonable():
    for latitude in (l['latitude'] for l in LOCATIONS):
        yield assert_greater_equal, latitude, 53.3
        yield assert_less_equal, latitude, 53.5


def test_that_every_longitude_is_reasonable():
    for longitude in (l['longitude'] for l in LOCATIONS):
        yield assert_greater_equal, longitude, -3.0
        yield assert_less_equal, longitude, -2.9


def test_that_every_location_name_is_unicode_string():
    for name in (l['locationName'] for l in LOCATIONS):
        yield assert_is_instance, name, type('')


def test_that_every_location_name_is_non_empty():
    for name in (l['locationName'] for l in LOCATIONS):
        yield assert_not_equal, name, ''


def test_that_every_location_name_has_no_stray_whitespace():
    for name in (l['locationName'] for l in LOCATIONS):
        yield assert_equal, name, name.strip()


def test_that_available_bikes_always_integer():
    for available_bikes in (l['availableBikes'] for l in LOCATIONS):
        yield assert_is_instance, available_bikes, int


def test_that_available_bikes_between_zero_and_fifteen():
    for available_bikes in (l['availableBikes'] for l in LOCATIONS):
        yield assert_greater_equal, available_bikes, 0
        yield assert_less_equal, available_bikes, 15


def test_that_available_locks_always_integer():
    for available_locks in (l['availableLocks'] for l in LOCATIONS):
        yield assert_is_instance, available_locks, int


def test_that_available_locks_between_zero_and_fifteen():
    for available_locks in (l['availableLocks'] for l in LOCATIONS):
        yield assert_greater_equal, available_locks, 0
        yield assert_less_equal, available_locks, 15


def test_that_first_location_is_correct():
    assert_equal(
        {
            'locationName': 'Pier Head Ferry Terminal',
            'availableBikes': 3,
            'availableLocks': 7,
            'latitude': 53.4051319444,
            'longitude': -2.9971558333
        },
        LOCATIONS[0])


def test_that_fifth_location_is_correct():
    assert_equal(
        {
            'locationName': 'Old Hall Street - The Capital Building',
            'availableBikes': 3,
            'availableLocks': 5,
            'latitude': 53.4091938889,
            'longitude': -2.9941066667
        },
        LOCATIONS[4])


def test_that_twenty_fifth_location_is_correct():
    assert_equal(
        {
            'locationName': 'Lime Street Railway Station',
            'availableBikes': 10,
            'availableLocks': 6,
            'latitude': 53.4071480556,
            'longitude': -2.9795275
        },
        LOCATIONS[24])


def test_that_last_location_is_correct():
    assert_equal(
        {
            'locationName': 'Wavertree Technology Park Station',
            'availableBikes': 4,
            'availableLocks': 8,
            'latitude': 53.405784,
            'longitude': -2.9228465
        },
        LOCATIONS[-1])
