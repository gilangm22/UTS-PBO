import sqlite3

# Fungsi untuk membuat tabel kontak jika belum ada
def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      phone TEXT,
                      email TEXT)''')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan kontak baru
def add_contact(name, phone, email):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    conn.close()

# Fungsi untuk melihat semua kontak
def view_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Fungsi untuk menjalankan aplikasi manajemen kontak
def main():
    create_table()
    while True:
        print("\n===== Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
            print("Contact added successfully!")
        elif choice == '2':
            contacts = view_contacts()
            if contacts:
                print("\n=== Contacts ===")
                for contact in contacts:
                    print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
            else:
                print("No contacts available.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
