while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("That is not a valid number. Try again...")