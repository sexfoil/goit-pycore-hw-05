def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def contact_exists(name, contacts):
    return name in contacts.values()


def add_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
        raise KeyError(f"Contact with name '{name}' already exists.")
    
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if not contacts.get(name):
        raise KeyError(f"Contact with name '{name}' does not exist.")
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name, = args

    if not contacts.get(name):
        raise KeyError(f"Contact with name '{name}' does not exist.")
        
    return  contacts.get(name)


def show_all(contacts):
    contacts_list = [f"{name:>15}: {contacts.get(name)}" for name in contacts.keys()]
    return "\n".join(contacts_list)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
            
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "add":
                    print(add_contact(args, contacts))

                case "change":
                    print(change_contact(args, contacts))

                case "phone":
                    print(show_phone(args, contacts))

                case "all":
                    print(show_all(contacts))

                case "hello":
                    print("How can I help you?")

                case "close" | "exit":
                    print("Good bye!")
                    break

                case _:
                    print("Invalid command.")
        except (KeyError, ValueError) as e:
            print(f"[ERROR]: {e}")


if __name__ == "__main__":
    main()
