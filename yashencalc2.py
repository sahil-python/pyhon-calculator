# Simple calculator

#Function adder
def adder(x, y):
   return x + y

# to subtract two numbers
def minus(x, y):
   return x - y

# this one will divide the two
def divide(x, y):
   return x / y

# this function multi
def multu(x, y):
   return x * y

print("Select Yashens Choices fucker.")
print("1.adder")
print("2.minus")
print("3.multu")
print("4.divide")

# Please enter input
RyansDevice = input("Enter Your side(4/3/2/1): ")

iNum1 = float(input("Enter your 1st Number: "))
iNum2 = float(input("Enter your 2st Number: "))

if RyansDevice == '1':
    print(iNum1, "+", iNum2, "=", adder(iNum1, iNum2))
elif RyansDevice == '2':
    print(iNum1, "-", iNum2, "=", minus(iNum1, iNum2))
elif RyansDevice == '3':
    print(iNum1, "*", iNum2, "=", multu(iNum1, iNum2))
elif RyansDevice == '4':
    print(iNum1, "/", iNum2, "=", divide(iNum1, iNum2))
else:
    print("Invalid input")
