# 🔍 SQL Injection Detector

A Python-based cybersecurity tool that scans Python source code for basic SQL Injection risks by identifying unsafe SQL query construction patterns.

---

## 📌 Overview

SQL Injection is one of the most common web application vulnerabilities. This project demonstrates how insecure SQL queries can be identified by scanning Python code for SQL statements combined with string concatenation.

> **Note:** This tool is intended for educational purposes. It performs simple pattern-based detection and is not a complete security scanner.

---

## ✨ Features

- 📂 Scans Python source code files
- 🔍 Detects SQL keywords:
  - SELECT
  - INSERT
  - UPDATE
  - DELETE
- ⚠️ Detects string concatenation (`+`) used in SQL queries
- 📍 Displays the line number where a potential issue is found
- 🚦 Displays a Risk Level (High/Low)
- 💡 Provides security recommendations

---

## 🛠 Technologies Used

- Python 3
- File Handling
- String Processing
- Loops
- Conditional Statements

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/gari426-beep/sql-injection-detector.git
```

Move into the project folder:

```bash
cd sql-injection-detector
```

---

## ▶️ Run the Program

```bash
python sql_detector.py
```

When prompted, enter the Python file you want to scan.

Example:

```text
sample_code.py
```

---

## 📁 Project Structure

```
sql-injection-detector/
│── sql_detector.py
│── sample_code.py
│── safe_code.py
│── README.md
│── requirements.txt
│── LICENSE
│── .gitignore
```

---

## 💻 Example Output

```
Enter the Python file to scan:
sample_code.py

File loaded successfully!

========== Scan Report ==========

SQL statement found on line 4
⚠️ Possible SQL Injection on line 4

========== Risk Level ==========
🔴 Risk Level: HIGH

========== Recommendation ==========
Use parameterized queries instead of string concatenation.
Avoid directly inserting user input into SQL queries.
```

---

## 🛡 Example of Unsafe Code

```python
username = input("Username: ")

query = "SELECT * FROM users WHERE username = '" + username + "'"
```

---

## ✅ Safer Approach

```python
cursor.execute(
    "SELECT * FROM users WHERE username = ?",
    (username,)
)
```

Using parameterized queries helps prevent SQL Injection attacks.

---

## ⚠️ Limitations

- Pattern-based detection only
- Does not execute or analyze SQL queries
- May miss complex cases
- Intended for learning purposes

---

## 🚀 Future Improvements

- Detect f-string SQL queries
- Detect `%` string formatting
- Export scan results to a report
- GUI version using Tkinter
- Support scanning multiple files
- Improve detection accuracy

---

## 👨‍💻 Author

**Gauri**

🎓 BCA Student

🛡️ Learning Cybersecurity & Python

GitHub: https://github.com/gari426-beep