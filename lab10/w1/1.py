import psycopg2
import csv

connection = psycopg2.connect( # Connecting to the PhoneBook db
    database = "PhoneBook",
    user = "postgres",
    password = "123789789",
    host = "localhost"
)

def create_table():

    command = """
            CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255),
            user_phone VARCHAR(20)
            )
        """
    with connection.cursor() as cur:
        # execute the command
        cur.execute(command)
    connection.commit() # save change to the db

def insert_user():

    user_name = input("Enter user name: ")
    user_phone = input("Enter user phone: ")

    command = """
        INSERT INTO users(user_name,user_phone) VALUES (%s,%s)
    """

    with connection.cursor() as cur:
        # execute the command
        cur.execute(command, (user_name,user_phone))

    connection.commit()
    print("\nuser added successfully!")

def insert_from_csv(file_path):

    with connection.cursor() as cur:
        with open(file_path,'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for row in csvreader:
                cur.execute("INSERT INTO users (user_name,user_phone) VALUES (%s,%s)",(row[0],row[1]))

        connection.commit()
        print("\nData from CSV added successfully!")
        
def update_user():
    name = input("Enter user_name to update: ")
    new_phone = input("Enter new phone number: ")

    command = "UPDATE users SET user_phone = %s WHERE user_name = %s"

    with connection.cursor() as cur:
        cur.execute(command, (new_phone,name))

    connection.commit()
    print("\nContact updated!")

def filter_by_first_letter():
    letter = input("Enter letter: ")
    command = " SELECT * FROM users WHERE user_name ILIKE %s"
  
    with connection.cursor() as cur: 
        cur.execute(command, (letter + '%',))
        results = cur.fetchall()
        for row in results:
            print(row)
    print("\nfiltering by first letter completed!")

def filter_by_part():
    keyword = input("Enter letters: ")
    command = "SELECT * FROM users WHERE user_name ILIKE %s"

    with connection.cursor() as cur:
        cur.execute(command,("%" + keyword + "%",))
        results = cur.fetchall()
        for row in results:
            print(row)

    print("\nfiltering by part completed!")

def delete_user():

    name = input("Enter a name to delete: ")

    command = "DELETE FROM users WHERE user_name = %s"

    with connection.cursor() as cur:
        cur.execute(command, (name,))

    connection.commit()
    print("\nContact deleted")

def truncate_table():
    command = "TRUNCATE TABLE users RESTART IDENTITY"

    with connection.cursor() as cyr:
        cyr.execute(command)

    connection.commit()

    print("\nThe table has been cleared!")

if __name__ == "__main__":
    create_table() # create a table if it doesn't exist yet

    while True:
        print("\n PHONEBOOK MENU: ")
        print("1. Add new user")
        print("2. Load users from CSV")
        print("3. Update user's phone")
        print("4. Filter by first letter")
        print("5. Filter by part")
        print("6. Delete user")
        print("7. Clear table")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            insert_user() 
        elif choice == '2':
            path_csv = input("Enter csv path: ")
            insert_from_csv(path_csv)
        elif choice == '3':
            update_user()
        elif choice == '4':
            filter_by_first_letter()
        elif choice == '5':
            filter_by_part()
        elif choice == '6':
            delete_user()
        elif choice == '7':
            truncate_table()
        elif choice == '0':
            print("You have exited the PhoneBook!")
            break
        else:
            print("Invalid option X")