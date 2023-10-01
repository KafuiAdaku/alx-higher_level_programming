#!/usr/bin/python3
"""A Python script that fetches `https://alx-intranet.hbtn.io/status`"""


if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        page = response.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        print(f"\t- utf8 content: {page.decode('utf-8')}")
