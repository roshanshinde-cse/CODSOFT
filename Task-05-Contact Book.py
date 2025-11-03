# Task-05-ContactBook/contact_book.py

contacts = {}

def show_menu():
    print("\n=== Contact Book Menu ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts yet!")
    else:
        for name, info in contacts.items():
            print(f"{name} - {info['phone']} - {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Found: {name} - {info['phone']} - {info['email']}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    show_menu()
    choice = input("Choose: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
