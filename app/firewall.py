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


def delete_rule():
    rules = load_rules()

    if not rules:
        print("\nNo firewall rules found.")
        return

    name = input("Enter rule name to delete: ").strip()

    if not name:
        print("Rule name cannot be empty.")
        return

    updated_rules = [
        rule for rule in rules
        if rule["name"].lower() != name.lower()
    ]

    if len(updated_rules) == len(rules):
        print("\nRule not found.")
        return

    save_rules(updated_rules)

    print("\nFirewall rule deleted successfully!")


def update_rule():
    rules = load_rules()

    if not rules:
        print("\nNo firewall rules found.")
        return

    name = input("Enter rule name to update: ").strip()

    if not name:
        print("Rule name cannot be empty.")
        return

    for rule in rules:
        if rule["name"].lower() == name.lower():

            print("\nCurrent Rule:")
            print(
                f"Name: {rule['name']} | "
                f"Protocol: {rule['protocol']} | "
                f"Port: {rule['port']} | "
                f"Action: {rule['action']}"
            )

            new_protocol = input(
                "Enter new protocol (TCP/UDP): "
            ).strip().upper()

            if new_protocol not in ("TCP", "UDP"):
                print("Invalid protocol. Use TCP or UDP.")
                return

            try:
                new_port = int(input("Enter new port: ").strip())
            except ValueError:
                print("Invalid port. Port must be a number.")
                return

            if not 1 <= new_port <= 65535:
                print(
                    "Invalid port. Enter a port between 1 and 65535."
                )
                return

            new_action = input(
                "Enter new action (ALLOW/DENY): "
            ).strip().upper()

            if new_action not in ("ALLOW", "DENY"):
                print("Invalid action. Use ALLOW or DENY.")
                return

            rule["protocol"] = new_protocol
            rule["port"] = new_port
            rule["action"] = new_action

            save_rules(rules)

            print("\nFirewall rule updated successfully!")
            return

    print("\nRule not found.")


def search_rules():
    rules = load_rules()

    if not rules:
        print("\nNo firewall rules found.")
        return

    keyword = input(
        "Enter name, protocol, port, or action to search: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = []

    for rule in rules:
        if (
            keyword in rule["name"].lower()
            or keyword == rule["protocol"].lower()
            or keyword == str(rule["port"])
            or keyword == rule["action"].lower()
        ):
            results.append(rule)

    print("\nSearch Results")
    print("-" * 60)

    if not results:
        print("No matching firewall rules found.")
        return

    for rule in results:
        print(
            f"Name: {rule['name']} | "
            f"Protocol: {rule['protocol']} | "
            f"Port: {rule['port']} | "
            f"Action: {rule['action']}"
        )