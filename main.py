from os import system
import time
import connection as conn

db = conn.DB()

# result = db.execute_query("SELECT * FROM users")
# print(result.fetchall())


def create():
    name = str(input("Name: "))
    email = str(input("Email: "))
    if(len(name) > 0 and len(email) > 0):
        sql = "INSERT INTO users(name,email) VALUES(?,?)"
        params = (name, email)
        db.execute_query(sql, params)
        print("User added successfully")
    else:
        print("Please type a name and an email.")


def read():
    pull = db.execute_query("SELECT * FROM users")
    print("\n\033[35mThese are the users registered:\033[0m")
    for data in pull:
        print(f'''
              ID: {data[0]}
              Name: {data[1]}
              Email: {data[2]}
              ''')


def update():
    id = int(input("Enter ID of user to update: "))
    if(id != 0):
        name = str(input("Name: "))
        email = str(input("Email: "))
        if(len(name) > 0 and len(email) > 0):
            sql = "UPDATE users SET name=?,email=? WHERE id=?"
            params = (name, email, id)
            db.execute_query(sql, params)
            print("User info updated.")
    else:
        print("An ID is required for this task.")


def delete():
    id = int(input("Enter ID of user to be deleted: "))
    if(id != 0):
        sql = "DELETE FROM users WHERE id=?"
        params = (id,)
        db.execute_query(sql, params)
        print(f"User {id} has been deleted!")
    else:
        print("An ID is required for this task.")


def search():
    name = str(input("Name of the user to search: "))
    if(len(name) > 0):
        sql = "SELECT * FROM users WHERE name LIKE ?"
        params = (f'%{name}%',)
        result = db.execute_query(sql, params)
        for data in result:
            print(f"""
\tID:        {data[0]}
\tNOMBRE:    {data[1]}
\tEMAIL:     {data[2]}""")


while True:
    print("\033[32m="*35)
    print("\tCRUD with SQLite3")
    print("="*35)
    print("\t[1] Create user")
    print("\t[2] View list of users")
    print("\t[3] Update user")
    print("\t[4] Delete user")
    print("\t[5] Search user")
    print("\t[6] Exit")
    print("="*35+"\033[0m")

    try:
        option = int(input("Select an option from menu: "))
        if(option == 1):
            create()
            time.sleep(1)
            system("clear")

        elif (option == 2):
            read()
            miniMenu = int(input("[1] Back to main menu\t[2] Exit:"))
            if(miniMenu == 1):
                time.sleep(1)
                system("clear")
            elif(miniMenu == 2):
                break

        elif (option == 3):
            update()
            time.sleep(1)
            system("clear")

        elif (option == 4):
            delete()
            time.sleep(1)
            system("clear")

        elif (option == 5):
            search()

        elif (option == 6):
            system("clear")
            break
    except:
        print("That's not an option, please try again.")
        system("clear")
