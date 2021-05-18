#  simple calculator

# Define function (add two numbers)
def add(x,y):
    return x + y

# Define function subtract
def sub(x,y):
    return x - y

def multi(x,y):
    return x*y

def divide(x,y):
    return x / y

print("Select Operation ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user

choice = input("Enter choice(1/2/3/4: ")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter second Number: "))

if choice == '1':
    print(num1, "+" , num2, "=" , add(num1, num2))

elif choice == '2':
    print(num1, "-" , num2, "=" , sub(num1, num2))

elif choice == '3':
    print(num1, "*" , num2, "=" , sub(num1, num2))

elif choice =='4':
    print(num1, "/" , num2 , "=" , divide(num1, num2))

else:
    print("Invalid Input")
1
