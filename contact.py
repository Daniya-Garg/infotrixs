class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

import json

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.file_name = "contacts.json"

    def save_contacts_to_file(self):
        with open(self.file_name, "w") as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def load_contacts_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.contacts = [Contact(contact["name"], contact["phone"], contact["email"]) for contact in data]
        except FileNotFoundError:
            pass

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts_to_file()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def update_contact(self, index, name, phone, email):
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email
            self.save_contacts_to_file()
            print("Contact updated successfully!")
        else:
            print("Invalid index. Contact not found.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts_to_file()
            print("Contact deleted successfully!")
        else:
            print("Invalid index. Contact not found.")

def main():
    contact_manager = ContactManager()
    contact_manager.load_contacts_from_file()

    while True:
        print("\nOptions:")
        print("1 - Add Contact")
        print("2 - View Contacts")
        print("3 - Update Contact")
        print("4 - Delete Contact")
        print("5 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.update_contact(index, name, phone, email)

        elif choice == "4":
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)

        elif choice == "5":
            print("Exiting")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
