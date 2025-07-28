import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact.to_dict())
        self.save_contacts()
        print(f"Added contact: {name} Phone: {phone} | Email: {email}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContacts List:")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact['name']} Phone: {contact['phone']} | Email: {contact['email']}")

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)

def main():
    manager = ContactManager()
    while True:
        print("\nContact Manager CLI")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Select option: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

