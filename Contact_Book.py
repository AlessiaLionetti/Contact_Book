import csv
import os

Contacts = "contact.csv"

if not os.path.exists(Contacts):
    with open(Contacts, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone','Email'])

while True:
    print('\nContact Book')
    print('1. Add Contact')
    print('2. View Contacts')
    print('3. Search Contact')
    print('4. Delete Contact')
    print('5. Exit')

    choice = input('Enter your choice (1-5): ')

    if choice == "1":
        name = input('Enter a name: ')
        phone = input('Enter phone: ')
        email = input('Enter email: ')

        with open(Contacts, mode='a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])

    elif choice == '2':

        with open(Contacts, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))

    elif choice == '3':

        search_name = input('Enter a name: ')

        with open(Contacts, mode='r') as file:
            reader = csv.reader(file)
            next(reader) #to skip header

            found = False
            for row in reader:
                if search_name in row[0]:
                    print(" | ".join(row))
                    found = True

            if not found:
                print("no contacts found with that name")

    elif choice == '4':

        delete_contact = input('Please enter the full name of the contact you need to delete: ')

        with open(Contacts, mode='r') as file:
            reader = csv.reader(file)
            contacts = list(reader) #read all rows as list

            new_contacts = []
            found2 = False
            for row in contacts:
                if row[0] == delete_contact:
                    found2 = True
                else:
                    new_contacts.append(row)

        with open(Contacts, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_contacts)

    elif choice == '5':
        break

'''
Alternative way to create a new csv file without importing operating system

import csv

Contacts = "contact.csv"

# Try to open the file in read mode to check if it exists
try:
    with open(Contacts, mode='r') as file:
        pass  
except FileNotFoundError:
    # File doesn't exist, so create it and write the header
    with open(Contacts, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email'])
'''
