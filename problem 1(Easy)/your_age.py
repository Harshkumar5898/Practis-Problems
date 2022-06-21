def age(aage, ayear):

    if int(aage) < 100:
        time_left_to_turn_100 = 100-aage
        year = ayear+time_left_to_turn_100
        print(f"In year {year} you turn hundred")

    if int(aage) == 100:
        print("You already turned 100 this year")

    elif int(aage) > 100:
        time_left_to_turn_100 = 100-aage
        year = ayear+time_left_to_turn_100
        print(f"You already turned 100 in year {year}")


def year(aage, ayear):
    year = aage+100
    if year > ayear:
        print(f"You turn 100 in year {year}")

    elif year == ayear:
        print("You already turned 100 this year")

    elif year < ayear:
        print(f"You already turned 100 in year {year}")


def age_in_year(aage, ayear):
    try:
        if aage <= 125:
            iyear = int(
                input("Enter a perticular year to know your age in that year : "))
            age = aage + (iyear - ayear)
            print(f"Your age in year {iyear} is {age}")

        elif aage > 1900:
            iyear = int(
                input("Enter a perticular year to know your age in that year : "))
            age = iyear - aage
            print(f"Your age in year {iyear} is {age}")

    except Exception as e:
        print("please enter a valid year only")


while True:
    person_age = input("Enter your todays age or year of birth : ")
    todays_year = input("Enter what is this year : ")

    if person_age.isnumeric() and todays_year.isnumeric():
        person_age = int(person_age)
        todays_year = int(todays_year)

    else:
        print("Tey Again latter!, Please enter a valid input.")
        continue

    if person_age <= 125:
        age(person_age, todays_year)

    elif person_age >= 1900 and person_age <= todays_year:
        year(person_age, todays_year)

    elif person_age > 125 and person_age <= 1000:
        print(f"You seem to be oldest person alive")
        print("Try Again Latter!, Please enter a valid age or year.")
        continue

    elif person_age > 1000 and person_age < 1900 or person_age > todays_year:
        print("You are not born yet")
        print("Try Again Latter!, Please enter a valid age or year.")
        continue

    print("Do you want to know your age in a perticular year enter y to yes else enter any key")
    a = input()
    if a == 'y':
        age_in_year(person_age, todays_year)

    else:
        exit()
