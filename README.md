# 🔥 Firewall Rule Automation Pro

[![Python Tests](https://github.com/syedashfaqali75-debug/Firewall-Rule-Automation-Pro/actions/workflows/python-tests.yml/badge.svg)](https://github.com/syedashfaqali75-debug/Firewall-Rule-Automation-Pro/actions/workflows/python-tests.yml)

A Python-based firewall rule automation and management tool designed to create, manage, validate, search, update, and delete firewall rules using a structured JSON configuration system.

The project demonstrates practical Python development, modular architecture, data validation, logging, automated testing, and GitHub Actions CI.

---

## 🚀 Features

- ✅ Add firewall rules
- ✅ List all firewall rules
- ✅ Update/Edit existing firewall rules
- ✅ Search and filter firewall rules
- ✅ Delete firewall rules
- ✅ TCP and UDP protocol support
- ✅ ALLOW and DENY actions
- ✅ Port validation from 1–65535
- ✅ Duplicate rule-name prevention
- ✅ JSON-based rule storage
- ✅ Application logging
- ✅ Automated tests with pytest
- ✅ GitHub Actions CI
- ✅ Modular Python project structure

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Pytest
- Git
- GitHub
- GitHub Actions
- PowerShell

---

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
│   ├── main.py
│   ├── firewall.py
│   ├── rules.py
│   └── logger.py
│
├── config/
│   └── rules.json
│
├── logs/
│   └── firewall.log
│
├── tests/
│   └── test_rules.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
