from zapv2 import ZAPv2
import time
import requests

ZAP_API = "http://127.0.0.1:8090"


def is_zap_running():
    try:
        requests.get(ZAP_API, timeout=2)
        return True
    except:
        return False


def zap_scan(target):
    results = []

    if not is_zap_running():
        return [{
            "name": "ZAP Passive Scan",
            "severity": "Low",
            "description": "OWASP ZAP is not running. Passive scan skipped."
        }]

    zap = ZAPv2(apikey=None, proxies={
        'http': ZAP_API,
        'https': ZAP_API
    })

    zap.urlopen(target)
    time.sleep(2)

    alerts = zap.core.alerts(baseurl=target)

    for alert in alerts:
        results.append({
            "name": alert.get("alert"),
            "severity": alert.get("risk"),
            "description": alert.get("desc")
        })

    return results
