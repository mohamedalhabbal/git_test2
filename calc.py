print("this is a calculator")


x = input("Num 1: ")
y = input("Num 2: ")
x = float(x)
y = float(y)
cal = input("Please choose one of the following: + - * /  **  %:")

if cal == "+":
    print(x + y)
elif cal == "-":
    print(x - y)
elif cal == "*":
    print(x * y)
elif cal == "/":
    print(x / y)
elif cal == "**":
    print(x ** y)
elif cal == "%":
    print(x % y)


else:
    print("Invalid Syntax")
