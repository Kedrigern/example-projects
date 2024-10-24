"""
Checks bunch of urls
"""

import asyncio
import requests

async def checkUrl(url: str) -> None:
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"[FAIL] connection error to domain {url}")
        return

    match r.status_code:
        case 200:
            print(f"[OK] {url}")
        case 300:
            print(f"[WARN] redirected {url}") # But to where?
        case _:
             print(f"[FAIL] bad code: {code} for {url}")


async def main() -> None:
    urls = [
        "https://httpstat.us/200",
        "https://httpstat.us/300",
        "https://httpstat.us/400",
        "https://httpstat.us/500",
        "https://www.python.org/",
        "https://www.python.cz/",
        "https://pythex.org/",
        "https://pyladies.cz/",#,
        "https://pyladies.czz/"
    ]

    tasks = []

    for url in urls:
        tasks.push(asyncio.create_task(checkUrl(url)))

    await asyncio.gather(tasks)

asyncio.run(main())
