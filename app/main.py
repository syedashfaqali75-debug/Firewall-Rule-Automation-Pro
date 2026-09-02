from app.firewall import list_rules, add_rule, delete_rule
from app.logger import setup_logger


def main():
    logger = setup_logger("Firewall Rule Automation Tool")

    while True:
        print("\n=== Firewall Rule Automation Tool ===")
        print("1. List firewall rules")
        print("2. Add firewall rule")
        print("3. Delete firewall rule")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_rules()

        elif choice == "2":
            add_rule()

        elif choice == "3":
            delete_rule()

        elif choice == "4":
            logger.info("Application closed.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()