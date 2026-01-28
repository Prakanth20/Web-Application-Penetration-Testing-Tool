import requests

def check_http_methods(url):
    methods = ["PUT", "DELETE", "OPTIONS"]
    allowed = []

    for m in methods:
        r = requests.request(m, url)
        if r.status_code < 400:
            allowed.append(m)

    if allowed:
        return {
            "name": "Insecure HTTP Methods",
            "description": f"Allowed methods: {', '.join(allowed)}",
            "severity": "Medium"
        }
    return None
