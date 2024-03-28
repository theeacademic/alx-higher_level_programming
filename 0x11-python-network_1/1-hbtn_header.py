#!/usr/bin/python3
import urllib.request
import sys

def fetch_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            x_request_id = headers.get('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id value: {x_request_id}")
            else:
                print("X-Request-Id not found in response headers.")
    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e.reason}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]
    fetch_x_request_id(url_to_fetch)

