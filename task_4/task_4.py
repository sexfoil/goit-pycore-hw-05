import re

phone_number_pattern = re.compile(r"\(\d{3}\)\d{3}-\d{2}-\d{2}")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()    
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"[ERROR] Data inconsistency: {e}"
        except ValueError as e:            
            return f"[ERROR] Unsupported format: {e}"
        except IndexError as e:
            return f"[ERROR] Arguments mismatch: {e}"

    return inner


def validate_arguments(args, expected):
    if len(args) != expected:
        raise IndexError(f"Arguments: expected='1', provided='{len(args)}'.")


def validate_phone(phone):
    if not phone_number_pattern.match(phone):
        raise ValueError(f"Phone number format: expected='(XXX)XXX-XX-XX', provided='{phone}'.")
    

def validate_contact(name, contacts):
    if not contacts.get(name):
        raise KeyError(f"Contact with name '{name}' does not exist.")
    

@input_error
def add_contact(args, contacts):
    validate_arguments(args, 2)
    
    name, phone = args
    if contacts.get(name):
        raise KeyError(f"Contact with name '{name}' already exists.")
    
    validate_phone(phone)

    contacts[name] = phone    
    return "Contact added."


@input_error
def change_contact(args, contacts):
    validate_arguments(args, 2)
    
    name, phone = args

    validate_phone(phone)
    validate_contact(name, contacts)    
    
    contacts[name] = phone    
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    validate_arguments(args, 1)
    
    name, = args 

    validate_contact(name, contacts)
    return contacts[name]


def show_all(contacts):
    size = 20
    dash_row = "-" * (size * 2 + 1)
    header = [dash_row, f"{'NAME':^{size}}|{'PHONE':^{size}}", dash_row]
    contacts_list = header + [f"{name:<{size}}|{contacts.get(name):^{size}}" for name in contacts.keys()]    
    return "\n".join(contacts_list)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
            
    while True:
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


if __name__ == "__main__":
    main()
