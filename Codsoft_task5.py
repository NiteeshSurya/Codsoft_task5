import sys

# A simple in-memory storage for contacts
contacts = []

def add_contact():
    print("\nAdd New Contact")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return
    
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\nSearch Contact")
    search_term = input("Enter name or phone number to search: ")
    
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone Number: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No contact found.")

def update_contact():
    print("\nUpdate Contact")
    search_term = input("Enter name or phone number of the contact to update: ")
    
    for contact in contacts:
        if search_term == contact['name'] or search_term == contact['phone']:
            print("Leave field blank to keep current value.")
            name = input(f"New Name [{contact['name']}]: ") or contact['name']
            phone = input(f"New Phone Number [{contact['phone']}]: ") or contact['phone']
            email = input(f"New Email [{contact['email']}]: ") or contact['email']
            address = input(f"New Address [{contact['address']}]: ") or contact['address']
            
            contact['name'] = name
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            
            print("Contact updated successfully!")
            return
    
    print("No contact found.")

def delete_contact():
    print("\nDelete Contact")
    search_term = input("Enter name or phone number of the contact to delete: ")
    
    for contact in contacts:
        if search_term == contact['name'] or search_term == contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    
    print("No contact found.")

def main_menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
