from app.rules import load_rules, save_rules


def list_rules():
    rules = load_rules()

    print("\nFirewall Rules")
    print("-" * 60)

    if not rules:
        print("No firewall rules found.")
        return

    for rule in rules:
        print(
            f"Name: {rule['name']} | "
            f"Protocol: {rule['protocol']} | "
            f"Port: {rule['port']} | "
            f"Action: {rule['action']}"
        )


def add_rule():
    rules = load_rules()

    name = input("Enter rule name: ").strip()

    if not name:
        print("Rule name cannot be empty.")
        return

    protocol = input("Enter protocol (TCP/UDP): ").strip().upper()

    if protocol not in ("TCP", "UDP"):
        print("Invalid protocol. Use TCP or UDP.")
        return

    try:
        port = int(input("Enter port: ").strip())
    except ValueError:
        print("Invalid port. Port must be a number.")
        return

    if not 1 <= port <= 65535:
        print("Invalid port. Enter a port between 1 and 65535.")
        return

    action = input("Enter action (ALLOW/DENY): ").strip().upper()

    if action not in ("ALLOW", "DENY"):
        print("Invalid action. Use ALLOW or DENY.")
        return

    for rule in rules:
        if rule["name"].lower() == name.lower():
            print("A rule with this name already exists.")
            return

    new_rule = {
        "name": name,
        "protocol": protocol,
        "port": port,
        "action": action
    }

    rules.append(new_rule)
    save_rules(rules)

    print("\nFirewall rule added successfully!")