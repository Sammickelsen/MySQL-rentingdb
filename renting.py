import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Obvious13",
  database="rentingdb"
)

mycursor = mydb.cursor()

def delete(type, id):
    if type == "Listing":
        
        mycursor.execute("""SELECT * FROM listings
                         WHERE seller_id = %s""", (id, ))
        results = mycursor.fetchall()

        print("Which Listing would you like to delete? \n(Select the number shown next to the listing)")
        for x in results:
            print(f"   {x[0]}. {x[1]}, ${x[2]}")
        delete_choice = int(input("\n> "))

        mycursor.execute("""DELETE FROM listings
                         WHERE listings_id = %s""", (delete_choice, ))

    elif type == "Request":

        mycursor.execute("""SELECT * FROM requests
                         WHERE renter_id = %s""", (id, ))
        results = mycursor.fetchall()

        print("Which Request would you like to delete? \n(Select the number shown next to the request)")
        for x in results:
            print(f"   {x[0]}. {x[1]}")
        delete_choice = int(input("\n> "))

        mycursor.execute("""DELETE FROM requests
                         WHERE requests_id = %s""", (delete_choice, ))
        

def view_requests():
    search = input("What state code do you want to search in: ")

    mycursor.execute("""SELECT request_name, city, state
                      FROM requests r JOIN renter re
                      ON r.renter_id = re.renter_id
                      WHERE state = %s;""", (search, ))
    results = mycursor.fetchall()
    print("\n\n")
    for i in results:
        print(f"{i[0]}, {i[1]}, {i[2]}")

def search_listings():
    search = input("What would you like to rent: ")

    mycursor.execute("""SELECT item, price, city, state
                     FROM listings l JOIN sellers s
                     ON l.sellers_id = s.sellers_id
                     WHERE item = %s """, (search, ))
    result = mycursor.fetchall()
    
    print("\n\n")
    for i in result:
        print(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}")

def create_listing(sellers_id):
    item = input("What is the name of the item you would like to rent out: ")
    price = input("How much would you like to rent the item for (Per Hour): ")

    mycursor.execute("""INSERT INTO listings (item, price, sellers_id)
                     VALUES (%s, %s, %s)""", (item, price, sellers_id))
    mydb.commit()
    print("Listing Created")

def create_request(renter_id):
    request_name = input("What type of vehicle would you like someone to rent out (ATV, Dirtbike, Paddleboards, etc.): ")

    mycursor.execute("""INSERT INTO Requests (request_name, renter_id)
                     VALUES (%s, %s)""", (request_name, renter_id))
    mydb.commit()
    print("Request Created!")

def create_seller():
    fname = input("What is your first name: ")
    lname =input("What is your last name: ")
    street = input("What is your street address: ")
    city = input("What city do you live in: ")
    state = input("Please input your state abbreviation (ex. CA, FL, ID): ")
    password = input("Please create a password you will remember: ")

    mycursor.execute("""INSERT INTO Sellers (fname, lname, street_address, city, state, password)
                     VALUES (%s, %s, %s, %s, %s, %s)""", (fname, lname, street, city, state, password))
    mydb.commit()

    mycursor.execute("SELECT sellers_id FROM Sellers WHERE fname = %s AND password = %s", (fname, password))
    result = mycursor.fetchall()

    for i in result:
        id = int(i[0])
    return id

def create_renter():
    fname = input("What is your first name: ")
    lname =input("What is your last name: ")
    city = input("What city do you live in: ")
    state = input("Please input your state abbreviation (ex. CA, FL, ID): ")
    password = input("Please create a password you will remember: ")

    mycursor.execute("""INSERT INTO Renter (fname, lname, city, state, password)
                VALUES (%s, %s, %s, %s, %s)""", (fname, lname, city, state, password))
    mydb.commit()

    mycursor.execute("SELECT renter_id FROM Renter WHERE fname = %s AND password = %s", (fname, password))
    result = mycursor.fetchall()

    for i in result:
        id = int(i[0])
    return id

def login(table):
    print("Please log in:")
    fname = input("What is your first name: ")
    password = input("What is your password: ")
    
    if table == "Renter":
        mycursor.execute("SELECT renter_id FROM Renter WHERE fname = %s AND password = %s", (fname, password))
        result = mycursor.fetchall()
    elif table == "Seller":
        mycursor.execute("SELECT sellers_id FROM Sellers WHERE fname = %s AND password = %s", (fname, password))
        result = mycursor.fetchall()

    if len(result) > 0:
        for i in result:
            id = int(i[0])
        return id
    else:
        print("Unknown username or password.")
        return 0

print("""Are you renting or selling?
      1. Renting
      2. Selling
      """)
option = input("> ")
sign_in = True

while sign_in == True:
    if option == '1':
        user_id = 0
        while user_id == 0:
            print("\nDo you have an account? (y/n)")
            account_made =  input("> ")
            if account_made.lower() == "y":
                user_id = login("Renter")
                user_type = "Renter"
            elif account_made.lower() == 'n':
                user_id = create_renter()
                user_type = "Renter"
            else:
                print("Not a valid response")
        sign_in = False

    elif option == '2':
        user_id = 0
        while user_id == 0:
            print("\nDo you have an account? (y/n)")
            account_made = input("> ")
            if account_made.lower() == "y":
                user_id = login("Seller")
                user_type = "Seller"
            elif account_made.lower() == 'n':
                user_id = create_seller()
                user_type = "Seller"
            else:
                print("Not a valid response")
        sign_in = False
    else:
        print("Not a valid response.")

renter_loop = True
seller_loop = True

if user_type == "Renter":
    while renter_loop == True:
        print("\n\nWelcome, Renter! What would you like to do?")
        print(" 1. Make Request\n 2. Search Listings\n 3. Delete Requests\n 4. Quit")
        rent_choice = input("> ")

        if rent_choice == '1':
            create_request(user_id)
        elif rent_choice == '2':
            search_listings()
        elif rent_choice == '3':
            delete("Request", user_id)
        elif rent_choice == '4':
            print("Goodbye!")
            renter_loop = False

elif user_type == "Seller":
    while seller_loop == True:
        print("\n\nWelcome, Seller! What would you like to do?")
        print(" 1. Make Listing\n 2. View Requests Nearby\n 3. Quit")
        sell_choice = input("> ")

        if sell_choice == "1":
            create_listing(user_id)
        elif sell_choice == "2":
            view_requests()
        elif sell_choice == "3":
            delete("Listing", user_id)
        elif sell_choice == "4":
            print("Goodbye!")
            seller_loop = False