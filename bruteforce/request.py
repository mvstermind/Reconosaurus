from concurrent.futures import ThreadPoolExecutor, as_completed
from http import HTTPStatus
from urllib.parse import urlparse

import requests


def wordlist_to_urls(wordlist: list[str], url: str) -> list[str]:
    """
    Takes a wordlist list[str] and forms urls prepated to be used
    for sending requests
    """
    if not url.startswith("https://") and not url.startswith("http://"):
        try:
            r = requests.get(f"https://{url}/")
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


def brute_force_with_dirs(urls: list[str], max_workers: int = 10) -> dict[str, int]:
    """
    Sends requests concurently using ThreadPoolExecutor to given list of urls
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
                return (get_path_only(url), r.status_code)
        except Exception:
            return None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fetch_status, url): url for url in urls}
        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                path, status_code = result
                valid_resp_with_status[path] = status_code

    return valid_resp_with_status


def get_path_only(link: str) -> str:
    """
    Returns only /path part from url
    """
    parsed_link = urlparse(link)
    path = parsed_link.path
    return path
