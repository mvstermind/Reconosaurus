"""
Responsible handling requests
"""

import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from http import HTTPStatus
from urllib.parse import urlparse

import requests

from prettify import colorify


def wordlist_to_urls(wordlist: list[str], url: str) -> list[str]:
    """
    Takes a wordlist list[str] and forms urls prepated to be used
    for sending requests

    wordlist: list[str] -> list of words that will be used to build url with
    url: str -> base url used to concatenate with wordlist

    returns list[str] -> list of urls combined with wordlist
    """
    if not url.startswith("https://") and not url.startswith("http://"):
        try:
            r = requests.get(f"https://{url}")
            if (
                r.status_code == HTTPStatus.OK
                or r.status_code >= 300
                and r.status_code < 400
            ):
                url = f"https://{url}"
        except Exception:
            r = requests.get(f"http://{url}")
            if (
                r.status_code == HTTPStatus.OK
                or r.status_code >= 300
                and r.status_code < 400
            ):
                url = f"http://{url}"

    urls: list[str] = []
    for word in wordlist:
        urls.append(f"{url}/{word}")

    return urls


def brute_force_w_dir(urls: list[str], max_workers: int = 10) -> dict[str, int]:
    """
    Sends requests concurently using ThreadPoolExecutor to given list of urls
    return only urls that responded with 200 or number between 300-400

    urls: list[str] -> formed urls that are used for iterating and sending requests
    max_workers:int -> number of threads to run

    returns: dict[str,int] -> returns dictionary of directories as keys with
    thier status codes as values

    if KeyboardInterrupt exception happens, kill whole program
    """
    valid_resp_with_status: dict[str, int] = {}

    def fetch_status(url: str):
        try:
            r = requests.get(url)
            if (
                r.status_code == HTTPStatus.OK
                or r.status_code >= 300
                and r.status_code < 400
            ):
                colorify.positive("Found paths:", end="")
                colorify.positive(f"{url} - Status Code: {r.status_code}")
                return (get_path_only(url), r.status_code)
        except Exception:
            return None

    try:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {executor.submit(fetch_status, url): url for url in urls}
            for future in as_completed(future_to_url):
                result = future.result()
                if result:
                    path, status_code = result
                    valid_resp_with_status[path] = status_code
    except KeyboardInterrupt:
        colorify.negative("\nExitting...")
        sys.exit()

    return valid_resp_with_status


def get_path_only(link: str) -> str:
    """
    Returns only /path part from url
    link: str -> full url eg https://foo.com/bar

    returns :str -> just path from url
    following example, this will return /bar
    """
    parsed_link = urlparse(link)
    path = parsed_link.path
    return path
