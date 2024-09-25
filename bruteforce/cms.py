from typing import Optional, Tuple

import requests
from requests.structures import CaseInsensitiveDict

from prettify import colorify


def detect(url: str) -> str:
    html, headers = fetch_site(url)
    if headers != None:
        if html is None:
            colorify.negative("Unable to detect CMS")

        else:
            if check_wordpress(html, headers):
                colorify.positive("WordPress detected")
                return "WordPress detected"

            elif check_joomla(html):
                colorify.positive("Joomla detected")
                return "Joomla detected"

            elif check_magento(html, headers):
                colorify.positive("Magento detected")
                return "Magento detected"
            else:
                colorify.negative("No CMS detected")
                return "No CMS detected"
    else:
        colorify.negative("No CMS detected")
        return "No CMS detected"


def fetch_site(url: str) -> Tuple[Optional[str], Optional[CaseInsensitiveDict[str]]]:
    try:
        response = requests.get(url)
        return response.text, response.headers
    except Exception as e:
        colorify.negative(f"Error fetching site: {e}")
        return None, None


def check_wordpress(html: str, headers: CaseInsensitiveDict[str]) -> bool:
    if "wp-content" in html or "wp-json" in html:
        return True
    if "X-Pingback" in headers or "/xmlrpc.php" in html:
        return True
    return False


def check_joomla(html: str) -> bool:
    if "index.php?option=com_" in html or "/templates/" in html:
        return True
    return False


def check_magento(html: str, headers: CaseInsensitiveDict[str]) -> bool:
    if "mage-" in html or "Magento" in headers.get("X-Generator", ""):
        return True
    return False
