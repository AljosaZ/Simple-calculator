print("Welcome to my simple calculator! \n")

count = 0
while True:
    if count == 6:
        print("\nWas that really that hard?")
        quit()
    else:
        try:
            x = float(input("Please enter the first number: "))
            break
        except ValueError:
            print("Please choose a number!")
        count += 1
while True:
    if count == 6:
        print("\nWas that really that hard?")
        quit()
    else:
        try:
            y = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Please choose a number!")
        count += 1

print("""
For addition choose: +
For substraction choose: -
For multiplication choose: *
For division choose: /
""")
count2 = 0
while True:
    if count2 ==6:
        print("\nWas that really that hard?")
        quit()
    else:
        try:
            action = input("Please insert operator (+, - ,*, /): ")

            if action == "+":
                print(f"{x} + {y} = {x+y}")
                break
            elif action == "-":
                print(f"{x} - {y} = {x-y}")
                break
            elif action == "*":
                print(f"{x} * {y} = {x*y}")
                break
            elif action == "/":
                if y == 0:
                    print("The denominator cannot equal 0!")
                    break
                else:
                    print(f"{x} / {y} = {round(x/y, 2)}")
                    break
            else:
                raise ValueError
        except ValueError:
            print("Please choose between availabe operators!")
            count2 += 1

print("\nWe did it!")