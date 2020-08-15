try:
    born_year = 0
    age = 0
    current_year = int(input("Enter the Current Year: "))
    if current_year < 2020:
        print("This Year Has Gone!, You are Living in Past. ")
        ext = input("Press Enter to Exit")
        exit()
    elif current_year > 3099:
        print(f"Sorry! This code is not made to work in {current_year}.")
        ext = input("Press Enter to Exit")
        exit()
    else:
        pass
    user_in = int(input("Enter Your Born Year or Your Current Age: "))


    if user_in > current_year:
        print("Sorry! You are Not Yet Born!")
        ext = input("Press Enter to Exit")
        exit()
    elif user_in < 0:
        print(f"{user_in} is Not a Valid Age! ")
        ext = input("Press Enter to Exit")
        exit()
    # elif (current_year - born_year) >= 150:
    #     print("You are Dead!")
    #     ext = input("Press Enter to Exit")
    #     exit()
    elif user_in <= 110:
        age = user_in
    elif user_in >= 1900 and user_in <= current_year:
        born_year = user_in
    elif user_in > 110 or user_in < 1900:
        print("This is Not a Valid Age Or Birth Year.")
        ext = input("Press Enter to Exit")
        exit()

    else:
        print("oops! Something went Wrong.")
        ext = input("Press Enter to Exit")
        exit()

    if born_year == 0:
        y100 = (current_year - age) + 100
        a = 100 - age
        print(f"you will be 100 years old after {a} Years, in {y100}")
    elif age == 0:
        a = 100 - (current_year - born_year )
        y100 = (born_year - age) + 100
        print(f"You Will be 100 Years old after {a} Years, in {y100} ")

    extra = input("\nDo You Want to check your Age in a Specific Year(Y/N): ")
    extra = extra.capitalize()
    while True:
        if extra == "Y":

            year = int(input("Enter the Year: "))
            if age == 0:
                agewill = year - born_year
                if agewill > 150:
                    print("Sorry! You are not Gonna Live that Long ")
                elif agewill < 0:
                    print("Invalid Input!")
                else:
                    print(f"You will be {agewill} Years Old in {year}")
                    break
            elif born_year == 0:
                agewill = age + (year - current_year)
                if agewill > 150:
                    print("Sorry! You are not Gonna Live that Long ")
                elif agewill < 0:
                    print("Invalid Input!")
                else:
                    print(f"You will be {agewill} Years Old in {year}")
                    break
        elif extra == "N":
            ext = input("Thanks for Using the tool \nPress Enter to Exit")
            exit()
        else:
            print("Invalid Input!")
        hold = input("Enter to Exit ")
        exit()
except ValueError:
    print("Invalid Input, Please Use Numbers Only")