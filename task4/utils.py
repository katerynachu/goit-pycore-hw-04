def parse_input(user_input):

    if not user_input.strip():
        return "", []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):

    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else :
        return "Contact not found"


def show_phone(args,contacts):

    if len(args) != 1:
        return "Invalid command. Please provide a contact name"
    
    name = args[0]
    if name in contacts:
        phone_number = contacts[name]
        return phone_number
    else:
        return "Contact not found"

def show_all(contacts):
    if not contacts:
        return "Your contact list is empty"
    result = "All contacts:\n"

    for name,phone in contacts.items():
        result+=f"{name}:{phone}\n"

    return result.strip()    




def main():
    pass
if __name__ == '__main__':
    main() 
