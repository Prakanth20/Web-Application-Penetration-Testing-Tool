import requests

def check_headers(url):
    r = requests.get(url)
    required = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security"
    ]

    missing = [h for h in required if h not in r.headers]

    if missing:
        return {
            "name": "Weak / Missing Security Headers",
            "description": "Missing: " + ", ".join(missing),
            "severity": "Low"
        }
    return None
