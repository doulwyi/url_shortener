import random
import re
import string

from models.url_shortener import UrlShortenModel


def create_hash():
    """
    Creates a unique hash for each URL.
    :return: Hash
    """
    _hash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    if UrlShortenModel.find_by_hash(_hash):
        create_hash()
    return _hash


def is_valid_url(url):
    """
    Check you URL is valid or not.
    :param url: Full URL provided by an user.
    :type url: str
    :return: True if matched or False if don't.
    """

    # extract from django code
    regex = re.compile(
        r'^(?:http)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if regex.match(url):
        return True
    else:
        return False
