from flask import Flask, render_template, request
from scanner import (
    headers_check, xss_check, sql_injection,
    directory_check, http_methods,
    https_check, misconfig_check,
    cvss, owasp_mapping
)
from scanner.zap_scanner import zap_scan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        results = []

        checks = [
            headers_check.check_headers,
            xss_check.check_xss,
            sql_injection.check_sqli,
            directory_check.check_open_directories,
            http_methods.check_http_methods,
            https_check.check_https,
            misconfig_check.check_misconfig
        ]

        for check in checks:
            output = check(url)
            if output:
                if isinstance(output, list):
                    results.extend(output)
                else:
                    results.append(output)

        # ZAP passive scan
        zap_results = zap_scan(url)
        results.extend(zap_results)

        for r in results:
            r["cvss"] = cvss.calculate_cvss(r["severity"])
            r["owasp"] = owasp_mapping.map_owasp(r["name"])

        return render_template("result.html", results=results, url=url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
