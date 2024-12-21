try:
    age = int(input("Enter your age: "))
    if age%2 == 0:
        print("Age is even")
    else:
        print("Age is odd")
except TypeError:
    print("Use numbers not letters")
except ValueError:
    print("Use whole numbers")