from os.path import dirname, join as pjoin

from .parse_html import parse_html


def get_latest_locations():
    fn = pjoin(dirname(__file__), 'sample_data', 'LocationsMap.aspx')
    with open(fn, 'r') as f:
        return list(parse_html(f))
