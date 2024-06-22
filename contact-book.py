import json

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(filename, contacts):
    with open(filename,  'w') as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone):
    contacts[name]  = phone

def view_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def remove_contacts(contacts, name):
    if name in contacts:
        del contacts[name]

filename = 'contacts.json'
contacts = load_contacts(filename)

while True:
    print("\nOptions:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Remove Contact")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        view_contacts(contacts)
    elif choice == 2:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(contacts, name, phone)
    elif choice == 3:
        name = input("Enter name to remove: ")
        remove_contacts(contacts, name)
    elif choice == 4:
        save_contacts(filename, contacts)
        break
    else:
        print("Invalid choice!")
