## 🔐 Web Application Penetration Testing Tool

A Flask-based web application designed to perform **basic automated penetration testing** on web applications.  
This tool is intended **strictly for educational and academic purposes** and is tested only on **intentionally vulnerable websites**.

---

## 📌 Features

- ✅ SQL Injection Detection (basic payload testing)
- ✅ Reflected Cross-Site Scripting (XSS) Detection
- ✅ Security Headers Analysis
- ✅ Missing HTTPS Detection
- ✅ Insecure HTTP Methods Detection
- ✅ Open Directory Detection
- ✅ Security Misconfiguration Checks
- ✅ CVSS Score Calculation
- ✅ OWASP Top 10 Mapping
- ✅ Optional OWASP ZAP Passive Scan Integration

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Requests
- OWASP ZAP API (optional)
- HTML, CSS (Frontend)

---

## 📂 Project Architecture

```

User Input (URL)
↓
Flask Web App
↓
Multiple Security Scanners
↓
Vulnerability Detection
↓
CVSS Scoring + OWASP Mapping
↓
Results Displayed in Web UI

````

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/web-pentest-tool.git
cd web-pentest-tool
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 🌐 Safe Test URLs (Recommended)

Only use **legal and intentionally vulnerable websites**:

* 🔹 [http://testphp.vulnweb.com/listproducts.php?cat=1](http://testphp.vulnweb.com/listproducts.php?cat=1)
* 🔹 [http://example.com](http://example.com)
* 🔹 [http://localhost:3000](http://localhost:3000) (OWASP Juice Shop - local)

❌ Do NOT test real websites without permission.

---

## 🧪 OWASP ZAP Integration (Optional)

### Start ZAP in daemon mode:

```bash
zap.bat -daemon -port 8090 -config api.disablekey=true
```

If ZAP is not running, the application **skips ZAP scanning gracefully**.

---

## 🎓 Academic Use Disclaimer

> This project is developed strictly for **educational purposes**.
> Testing was conducted only on **intentionally vulnerable applications** such as OWASP Juice Shop and Acunetix VulnWeb.

---

## 🧠 Future Enhancements

* Scan progress bar
* PDF report generation
* Authentication testing
* Stored XSS detection
* Role-based access
* Advanced CVSS vector calculation

---

## 👨‍💻 Author

**Prakanth V**
Cyber Security | Web Security | Python

---
