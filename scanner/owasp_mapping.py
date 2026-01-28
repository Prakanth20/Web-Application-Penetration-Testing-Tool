def map_owasp(name):
    mapping = {
        "SQL Injection": "A03:2021 – Injection",
        "Reflected XSS": "A07:2021 – Cross-Site Scripting",
        "Open Directory Listing": "A05:2021 – Security Misconfiguration",
        "Insecure HTTP Methods": "A05:2021 – Security Misconfiguration",
        "Missing HTTPS": "A02:2021 – Cryptographic Failures",
        "Weak / Missing Security Headers": "A05:2021 – Security Misconfiguration",
        "Security Misconfiguration": "A05:2021 – Security Misconfiguration"
    }
    return mapping.get(name, "Not Mapped")
