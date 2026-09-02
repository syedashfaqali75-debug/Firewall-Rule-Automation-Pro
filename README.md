# 🔥 Firewall Rule Automation Pro

A Python-based Firewall Rule Automation and Management Tool designed to manage firewall rules through a structured JSON configuration system.

The project demonstrates rule creation, validation, storage, logging, automated testing, and GitHub Actions CI.

---

## 🚀 Features

- ✅ Add firewall rules
- ✅ List firewall rules
- ✅ Delete firewall rules through the rule management module
- ✅ TCP and UDP protocol support
- ✅ ALLOW and DENY actions
- ✅ Port validation from 1 to 65535
- ✅ Duplicate rule-name prevention
- ✅ JSON-based rule configuration
- ✅ Application event logging
- ✅ Automated testing with pytest
- ✅ GitHub Actions CI
- ✅ Clean and modular project structure

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Pytest
- Git
- GitHub
- GitHub Actions

---

## 📁 Project Structure

```text
Firewall Rule Project/
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
│   └── .gitkeep
│
├── tests/
│   └── test_rules.py
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt