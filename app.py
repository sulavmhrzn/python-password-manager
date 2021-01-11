from utils.database import *
from utils.random_password import random_password
from heading import header

print(header)
CHOICE = "1. Create table\n2. Add application\n3. View all application\n4. Search applications\n0. Quit\n: "

choice = int(input(CHOICE))

while choice != 0:
    if choice in [1, 2, 3, 4]:
        if choice == 1:
            create_table()
        elif choice == 2:
            application_name = input("Application Name: ")
            url = input("URL: ")
            username = input("Username: ")
            password = random_password()
            insert_into_table(url, application_name, username, password)
        elif choice == 3:
            for result in get_all():
                print(
                    "URL: {} | Application name: {} | Username: {} | Password: {}".format(
                        result[1], result[2], result[3], result[4]
                    )
                )
        elif choice == 4:
            ch = int(input("1. Application name\n2. URL\n: "))
            if ch == 1:
                application_name = input("Application Name: ")
                for result in get_one(application_name):
                    print(
                        "URL: {} | Application name: {} | Username: {} | Password: {}".format(
                            result[1], result[2], result[3], result[4]
                        )
                    )
            elif ch == 2:
                url = input("URL: ")
                for result in get_one(url):
                    print(
                        "URL: {} | Application name: {} | Username: {} | Password: {}".format(
                            result[1], result[2], result[3], result[4]
                        )
                    )
        choice = int(input(CHOICE))
    else:
        print("Invalid options.")
        break