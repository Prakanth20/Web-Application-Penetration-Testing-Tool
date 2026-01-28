def check_https(url):
    if not url.startswith("https://"):
        return {
            "name": "Missing HTTPS",
            "description": "HTTPS is not enforced",
            "severity": "High"
        }
    return None
