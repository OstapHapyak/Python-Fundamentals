user_name = input("Enter your name: ")
user_age = float(input("Enter your age: "))
print(user_name, type(user_name))
print(user_age, type(user_age))

print ("Я великий пітоніст!")
print(1,2,3,4, sep='#', end='$')

amount = 1000
message = "Code is executed!"

if amount > 50:
    print("Hello Ostap!")
    print(message)
else: (print("Amounts is less than 50"),
       print(type(amount)))

f = 101
if f > 600 or f > 100:
    print(f)

a = 12; b = 12; c = 12
d = (a + b +
    c)
print(d)


print(a, b, sep= "space")
print(a, b, end= "done")




#Arithmetic operators
x = 11
y = 5

#output: x + y = 16
print("x + y =", x + y)

#output: x - y = 6
print("x - y =", x - y)

#output: x * y = 55
print("x * y =", x * y)

#output: x / y = 2.2
print("x / y =", x / y)

#output: x % y = 1
print("x % y =", x % y)

#output: x // y = 2
print("x // y =", x // y)

#output: x ** y = 161051
print("x ** y =", x ** y)


number_1 = 3 * 4 * 5 ** 2 + 7
print(number_1)

number_2 = (3 + 4) * (5 ** 2 + 7)
print(number_2)

number_3 = 2 ** 3 ** 2
print(number_3)

number_4 = (2 ** 3) **2
print(number_4)


name = str(input("What is your name? "))
print("Hello",name,"!")
age = int(input("How old are you? " ))
print("Your age is",age,".")
home = str(input("Where do you live? "))
print("You live in", home,".")

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

print(f"{a} + {b} =",a + b)
print(f"{a} - {b} =",a - b)
print(f"{a} * {b} =",a * b)
print(f"{a} / {b} =",a / b)
print(f"{a} // {b} =",a // b)
print(f"{a} % {b} =",a % b)
print(f"{a} **  {b} =",a ** b)