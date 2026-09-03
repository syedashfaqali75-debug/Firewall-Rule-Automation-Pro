from app.rules import load_rules, save_rules


def test_load_rules():
    rules = load_rules()
    assert isinstance(rules, list)


def test_save_and_load_rules(tmp_path):
    test_file = tmp_path / "rules.json"

    test_rules = [
        {
            "name": "Test Rule",
            "protocol": "TCP",
            "port": 8080,
            "action": "ALLOW"
        }
    ]

    import app.rules

    original_file = app.rules.RULES_FILE
    app.rules.RULES_FILE = str(test_file)

    save_rules(test_rules)
    loaded_rules = load_rules()

    assert loaded_rules == test_rules

    app.rules.RULES_FILE = original_file


def test_save_multiple_rules(tmp_path):
    test_file = tmp_path / "rules.json"

    test_rules = [
        {
            "name": "HTTP Rule",
            "protocol": "TCP",
            "port": 8080,
            "action": "ALLOW"
        },
        {
            "name": "DNS Rule",
            "protocol": "UDP",
            "port": 53,
            "action": "ALLOW"
        }
    ]

    import app.rules

    original_file = app.rules.RULES_FILE
    app.rules.RULES_FILE = str(test_file)

    save_rules(test_rules)
    loaded_rules = load_rules()

    assert len(loaded_rules) == 2
    assert loaded_rules[0]["name"] == "HTTP Rule"
    assert loaded_rules[1]["port"] == 53

    app.rules.RULES_FILE = original_file