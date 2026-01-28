import requests

def check_xss(url):
    payload = "<script>alert(1)</script>"
    r = requests.get(f"{url}?q={payload}")

    if payload in r.text:
        return {
            "name": "Reflected XSS",
            "description": "Input reflected without sanitization",
            "severity": "Medium"
        }
    return None
