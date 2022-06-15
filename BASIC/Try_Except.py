# CONTOH 1
number = int(input("Enter a number: "))
print(number)

# CONTOH 2
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

# CONTOH 3
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
