# Firewall Rule Automation Tool

A Python-based firewall rule automation and management tool for creating, viewing, and managing firewall rules using a JSON configuration file.

## Features

- Add firewall rules
- List firewall rules
- Delete firewall rules
- JSON-based rule configuration
- Logging of application events
- Automated testing with pytest
- Clean project structure

## Technologies Used

- Python
- JSON
- Pytest
- Git & GitHub

## Project Structure

```text
Firewall-Rule-Automation-Tool/
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
├── .gitignore
├── requirements.txt
└── README.md