"""
A menu - you need to add the database and fill in the functions. 
"""

import sqlite3

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS record_holders (
            name text PRIMARY KEY,
            catches integer
        )
    ''')

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records(conn)
        elif choice == '2':
            search_by_name(conn)
        elif choice == '3':
            add_new_record(conn)
        elif choice == '4':
            edit_existing_record(conn)
        elif choice == '5':
            delete_record(conn)
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')

    conn.commit()
    conn.close()

def display_all_records(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM record_holders')
    records = cursor.fetchall()
    if len(records) == 0:
        print("No records found")
    else:
        for record in records:
            print(record)

def search_by_name(conn):
    name = input('Enter the name of the record holder: ')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM record_holders WHERE name=?', (name,))
    record = cursor.fetchone()
    if record:
        print(record)
    else:
        print('No record found with the given name')

def add_new_record(conn):
    name = input('Enter the name of the record holder: ')
    catches = input('Enter the number of catches: ')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO record_holders (name, catches) VALUES (?,?)', (name, catches))
        print('Record added successfully')
    except sqlite3.IntegrityError:
        print('Record already exists with the given name')

def edit_existing_record(conn):
    name = input('Enter the name of the record holder: ')
    catches = input('Enter the new number of catches: ')
    cursor = conn.cursor()
    cursor.execute('UPDATE record_holders SET catches=? WHERE name=?', (catches, name))
    conn.commit()
    print('Record updated successfully')

def delete_record(conn):
    name = input('Enter the name of the record holder: ')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM record_holders WHERE name=?', (name,))
    conn.commit()
    print('Record deleted successfully')

if __name__ == '__main__':
    main()