# 🔥 Firewall Rule Automation Pro

A Python-based Firewall Rule Automation and Management Tool designed to create, manage, validate, search, update, and delete firewall rules using a structured JSON configuration system.

This project demonstrates practical Python development, modular architecture, data validation, logging, automated testing, and GitHub Actions CI.

## 🚀 Features

- ✅ Add firewall rules
- ✅ List all firewall rules
- ✅ Update/Edit existing firewall rules
- ✅ Delete firewall rules
- ✅ Search and filter firewall rules
- ✅ TCP and UDP protocol support
- ✅ ALLOW and DENY actions
- ✅ Port validation (1–65535)
- ✅ Duplicate rule-name prevention
- ✅ JSON-based rule storage
- ✅ Application logging
- ✅ Automated tests with pytest
- ✅ GitHub Actions CI

## 🛠️ Technologies Used

- Python 3
- Pytest
- JSON
- Git & GitHub
- GitHub Actions
- PowerShell
- Windows

## 📁 Project Structure

```text
Firewall-Rule-Automation-Pro/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── app/
│   ├── __init__.py
│   ├── firewall.py
│   ├── logger.py
│   ├── main.py
│   └── rules.py
│
├── config/
│   └── rules.json
│
├── tests/
│   └── test_rules.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
