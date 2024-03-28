#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}")
except urllib.error.URLError as e:
    print(f"Error fetching the URL: {e.reason}")

