import os
import getpass
import platform

import requests

import logging
logger = logging.getLogger(__name__)


def get_user_agent_header():
    """
    Return a user-agent from the environment, or a fairly revealing default
    user agent which aids debugging.
    """
    user_agent = os.environ.get('HTTP_USER_AGENT', default_user_agent())
    return {'User-Agent': user_agent}


def default_user_agent():
    username = getpass.getuser()
    hostname = platform.node()

    return '{} {user}@{hostname}'.format(
        requests.utils.default_user_agent(),
        user=username,
        hostname=hostname)
