from portal import bodyweight,  cardio,  plyometrics, login_page, portal_menu

while True:
    login_page()
    option = input("Choose an option: ")
    if option == "1":
        name = input("\nEnter name to register: \n")
        pin = input("\nEnter Pin \n")

        if len(name) < 1 or len(name) > 10:
            print("Name must be between 1 and 10 characters please")

        elif len(pin) != 4:
            print("Invalid Pin")
            continue

        else:
            print(f"\n{name} has been registered")
            print("\nPlease Login to start your workout")

    if option == "2":
        name = input("Enter your NAME: ")
        pin = input("Enter your PIN: ")

        if name == name and pin == pin:
            print("\nSuccessful Login!!\n")
            break

        else:
            print("\nInvalid Credentials, Try Again!!")

    if option == "3":
        print(f"Goodbye!")


while True:
    portal_menu(name)
    option = input("\nChoose your option ")

    if option == "1":
        bodyweight()

    elif option == "2":
        cardio()

    elif option == "3":
        plyometrics()

    elif option == "4":
        print(f"Goodbye {name}!\n")
        break
    else:
        ("\nInvalid Option\n")
