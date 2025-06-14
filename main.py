# Call https://is.gd/create.php
# https://is.gd/create.php?format=jsone&url=www.example.com
# https://is.gd/create.php?format=json&callback=myfunction&url=www.example.com

from urllib3 import request
from urllib3.util.retry import Retry
from urllib3.exceptions import MaxRetryError

urls = []
file_to_open = "urls.txt"

with open('urls.txt', 'r', encoding="utf-8") as url_file:
    for line in url_file:
        url = line.rstrip()
        if not url in urls:
            urls.append(url)

retry_configuration = Retry(
    status_forcelist=[400, 406, 502, 503],
    backoff_factor=0.1,
    backoff_max=30
)

for url in urls:
    try:
        r = request(
            method="GET",
            url="https://is.gd/create.php",
            fields={"format": "json", "url": url},
            retries=retry_configuration
        )

        match r.status:
            case 200:
                print(f"{r.json()["shorturl"]}, {url}")
            case _:
                print(f"error fetching {r.geturl()}")
                pass
    except MaxRetryError:
        print(f"error fetching {r.geturl()}")
        pass
