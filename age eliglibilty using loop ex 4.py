while True:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("Eligible")
    else:
        print("Not eligible")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() != "yes":
        break
