# 🔥 Firewall Rule Automation Pro

[![Python Tests](https://github.com/syedashfaqali75-debug/Firewall-Rule-Automation-Pro/actions/workflows/python-tests.yml/badge.svg)](https://github.com/syedashfaqali75-debug/Firewall-Rule-Automation-Pro/actions)

A Python-based firewall rule automation and management tool with validation, logging, JSON configuration, automated testing, and GitHub Actions CI.

## 🚀 Features

- Create and manage firewall rules
- Add, update, delete and search rules
- TCP and UDP protocol support
- ALLOW and DENY actions
- Port validation from 1–65535
- Duplicate rule-name prevention
- JSON-based configuration
- Logging
- Automated testing with Pytest
- Continuous Integration with GitHub Actions

## 🛠️ Technologies

- Python 3
- JSON
- Pytest
- Git
- GitHub
- GitHub Actions
- PowerShell

## 📁 Project Structure

```text
Firewall-Rule-Automation-Pro/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── firewall.py
│   ├── rules.py
│   └── logger.py
├── config/
│   └── rules.json
├── logs/
│   └── firewall.log
├── tests/
│   └── test_rules.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
