import requests

def check_open_directories(url):
    paths = ["/admin/", "/backup/", "/uploads/", "/test/"]
    findings = []

    for p in paths:
        r = requests.get(url.rstrip("/") + p)
        if r.status_code == 200 and "Index of" in r.text:
            findings.append({
                "name": "Open Directory Listing",
                "description": f"Directory listing enabled at {p}",
                "severity": "Medium"
            })
    return findings
