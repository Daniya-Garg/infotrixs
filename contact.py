import json

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.file_name = "contacts.json"
        self.load_contacts_from_file()

    def save_contacts_to_file(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file)

    def load_contacts_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

    def add_contact(self, name, phone, email):
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts_to_file()
        print("Contact added successfully!")

    def search_contact(self, name):
        matching_contacts = [contact for contact in self.contacts if contact["name"].lower() == name.lower()]
        return matching_contacts

    def update_contact(self, name, new_phone, new_email):
        matching_contacts = self.search_contact(name)
        if matching_contacts:
            for contact in matching_contacts:
                contact["phone"] = new_phone
                contact["email"] = new_email
            self.save_contacts_to_file()
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        matching_contacts = self.search_contact(name)
        if matching_contacts:
            self.contacts = [contact for contact in self.contacts if contact not in matching_contacts]
            self.save_contacts_to_file()
            print("Contact(s) deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nOptions:")
        print("1 - Add Contact")
        print("2 - Search Contact")
        print("3 - Update Contact")
        print("4 - Delete Contact")
        print("5 - View All Contacts")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to search: ")
            matching_contacts = contact_manager.search_contact(name)
            if matching_contacts:
                for contact in matching_contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("No matching contacts found.")

        elif choice == "3":
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            contact_manager.update_contact(name, new_phone, new_email)

        elif choice == "4":
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "5":
            if contact_manager.contacts:
                print("All Contacts:")
                for contact in contact_manager.contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("No contacts found.")

        elif choice == "6":
            print("Exiting")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
