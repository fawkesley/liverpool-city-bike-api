from io import StringIO

import logging
logger = logging.getLogger(__name__)

import requests

from .user_agent import get_user_agent_header


def download_html(export_url, gauge_identifier, start_date, end_date):
    headers = get_user_agent_header()

    response = requests.post(export_url, headers=headers, data={
        'startdate': start_date.strftime('%Y-%m-%d'),
        'enddate': end_date.strftime('%Y-%m-%d'),
        'datatype': gauge_identifier})
    response.raise_for_status()
    return StringIO(response.text)
