def calculate_cvss(severity):
    return {
        "Low": 3.1,
        "Medium": 6.1,
        "High": 8.8,
        "Critical": 9.8
    }.get(severity, 0.0)
