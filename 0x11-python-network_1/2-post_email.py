#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a `POST` request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in `utf-8`).
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')  # converts data to bytes

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
