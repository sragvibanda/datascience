"""

4. Write a function sum_of_integers(a, b) that takes two integers
 as input from the user and returns their sum.

"""

def sum_of_integers(a, b):
    a = int(input(a))
    while a != int(a):
        a = int(input(a))

    b = int(input(b))
    while b != int(b):
        b = int(input(b))

    sum = a + b
    return sum

def main():
    sum = sum_of_integers("Enter first number: ", "Enter second number: ")
    print("The sum of your numbers is:", sum)

main()



