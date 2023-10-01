#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to
    the URL and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except HTTPError as e:
        print("Error Code: ", e.code)
