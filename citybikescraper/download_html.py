try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO

import logging
logger = logging.getLogger(__name__)

import requests

from .user_agent import get_user_agent_header

MAP_URL = 'http://www.citybikeliverpool.co.uk/Mobile/LocationsMap.aspx'


def download_html():
    headers = get_user_agent_header()

    response = requests.get(MAP_URL, headers=headers)
    response.raise_for_status()
    return StringIO(response.text)
