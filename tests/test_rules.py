import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.rules import load_rules, add_rule, delete_rule


def test_load_rules():
    rules = load_rules()

    assert isinstance(rules, list)
    assert len(rules) >= 1


def test_add_rule():
    rules_before = load_rules()

    test_rule = {
        "name": "Test Rule",
        "protocol": "TCP",
        "port": 9999,
        "action": "DENY"
    }

    add_rule(test_rule)

    rules_after = load_rules()

    assert len(rules_after) == len(rules_before) + 1
    assert test_rule in rules_after

    # Clean up test rule
    delete_rule("Test Rule")


def test_delete_rule():
    test_rule = {
        "name": "Delete Test Rule",
        "protocol": "UDP",
        "port": 8888,
        "action": "DENY"
    }

    add_rule(test_rule)

    assert delete_rule("Delete Test Rule") is True

    rules = load_rules()

    assert test_rule not in rules