# main.py

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name},{self.phone},{self.email}"

    @staticmethod
    def from_string(contact_line):
        name, phone, email = contact_line.strip().split(',')
        return Contact(name, phone, email)

class ContactManager:
    def __init__(self, filename):
        self.filename = filename

    def add_contact(self, contact):
        with open(self.filename, 'a') as f:
            f.write(str(contact) + "\n")
        print("Contact added successfully!")

    def view_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                contacts = f.readlines()
            print("\nList of Contacts:")
            if not contacts:
                print("No contacts found.")
            for c in contacts:
                contact = Contact.from_string(c)
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        except FileNotFoundError:
            print("No contacts found.")

    def search_contact(self, keyword):
        found = False
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    contact = Contact.from_string(line)
                    if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
                        found = True
            if not found:
                print("Contact not found.")
        except FileNotFoundError:
            print("No contacts found.")

    def delete_contact(self, name):
        found = False
        try:
            with open(self.filename, 'r') as f:
                contacts = f.readlines()
            with open(self.filename, 'w') as f:
                for line in contacts:
                    contact = Contact.from_string(line)
                    if contact.name.lower() != name.lower():
                        f.write(str(contact) + "\n")
                    else:
                        found = True
            if found:
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")
        except FileNotFoundError:
            print("No contacts found.")

def main():
    filename = "contacts.txt"
    manager = ContactManager(filename)

    while True:
        print("\n----- Contact Management System -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone to search: ")
            manager.search_contact(keyword)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
