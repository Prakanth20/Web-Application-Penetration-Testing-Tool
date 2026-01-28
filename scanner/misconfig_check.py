import requests

def check_misconfig(url):
    r = requests.get(url)
    server = r.headers.get("Server")

    if server:
        return {
            "name": "Security Misconfiguration",
            "description": f"Server version exposed: {server}",
            "severity": "Low"
        }
    return None
