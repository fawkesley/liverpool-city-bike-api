from os.path import dirname, join as pjoin

from .download_html import download_html
from .parse_html import parse_html


def get_latest_locations():
    return list(parse_html(download_html()))
