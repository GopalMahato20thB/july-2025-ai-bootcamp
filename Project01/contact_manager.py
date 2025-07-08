import json
import os

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

# -------------------- Manager Class --------------------
class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact(d["name"], d["phone"]) for d in data]

    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def add_contact(self, name, phone):
        self.contacts.append(Contact(name, phone))
        print("✅ Contact added.")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts found.")
            return
        for i, c in enumerate(self.contacts, 1):
            print(f"{i}. {c.name} - {c.phone}")

    def search_contact(self, keyword):
        found = [c for c in self.contacts if keyword.lower() in c.name.lower()]
        if not found:
            print("🔍 No matching contact.")
        else:
            for i, c in enumerate(found, 1):
                print(f"{i}. {c.name} - {c.phone}")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                print(f"🗑️ Contact '{name}' deleted.")
                return
        print("❌ Contact not found.")

    def update_contact(self, name, new_phone):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                c.phone = new_phone
                print(f"✏️ Contact '{name}' updated.")
                return
        print("❌ Contact not found.")

# -------------------- Menu --------------------
def menu():
    manager = ContactManager()

    while True:
        print("\n--- 📇 Contact Manager ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Save & Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            manager.add_contact(name, phone)

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name to search: ")
            manager.search_contact(keyword)

        elif choice == "4":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)

        elif choice == "5":
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone: ")
            manager.update_contact(name, new_phone)

        elif choice == "6":
            manager.save_contacts()
            print("✅ All changes saved. Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

# -------------------- Run --------------------
menu()
