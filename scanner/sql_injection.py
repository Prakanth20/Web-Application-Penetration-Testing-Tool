import requests

def check_sqli(url):
    payload = "' OR '1'='1"
    r = requests.get(f"{url}?id={payload}")

    errors = ["sql", "mysql", "syntax error", "warning"]
    for e in errors:
        if e in r.text.lower():
            return {
                "name": "SQL Injection",
                "description": "SQL error detected with basic payload",
                "severity": "High"
            }
    return None
