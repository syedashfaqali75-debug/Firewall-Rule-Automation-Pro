import json
from pathlib import Path

RULES_FILE = Path(__file__).parent.parent / "config" / "rules.json"


def load_rules():
    """Load firewall rules from the JSON configuration file."""
    with open(RULES_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("rules", [])


def save_rules(rules):
    """Save firewall rules to the JSON configuration file."""
    with open(RULES_FILE, "w", encoding="utf-8") as file:
        json.dump({"rules": rules}, file, indent=2)


def add_rule(rule):
    """Add a new firewall rule."""
    rules = load_rules()
    rules.append(rule)
    save_rules(rules)


def delete_rule(rule_name):
    """Delete a firewall rule by name."""
    rules = load_rules()
    updated_rules = [
        rule for rule in rules
        if rule.get("name") != rule_name
    ]

    save_rules(updated_rules)
    return len(rules) != len(updated_rules)