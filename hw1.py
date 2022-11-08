# Name: Tanner Huck
# CSE 160
# Autumn 2022
# Homework 1

# importing "math" to make the math.sqrt function available
import math

# Problem 1
# printing out header for problem 1
print("Problem 1 solution follows:")

# Assigning a, b, and c the coeifficents from the quadratic
# equation we are trying
# to find the roots of.
a = 3
b = -5.86
c = 2.5408

# Calculating the value of the discriminant
discriminant = (b ** 2) - (4 * a * c)
# Calculating the negative and positive square roots of the discriminant
negative_discriminant = -math.sqrt(discriminant)
positive_discriminant = math.sqrt(discriminant)

# For loop that will take the negative and positive square roots
# of the discriminant and use the rest of the quadratic equation to solve
# for the roots.
index = 1  # index to hold which root we are calculating
for val_discriminant in [negative_discriminant, positive_discriminant]:
    root = (-b + val_discriminant) / (2 * a)  # calculating root
    print("Root " + str(index) + ":", root)  # printing out what the root is
    index = index + 1  # updating index

# Problem 2
# printing out header for problem 2
print("")
print("Problem 2 solution follows:")

# using a for loop that will go throught the values 2-10
for current_frac_val in range(2, 11):
    # printing out a fraction of 1 divided by the current range value
    # then printing out the decimal value of that fraction
    print("1/" + str(current_frac_val) + ":", 1/current_frac_val)

# Problem 3
# printing out header for problem 3
print("")
print("Problem 3 solution follows:")

# for loop to compute the 10th triangular number
# setting n to the nth triangular number we want, 10
n = 10
# variable triangular to hold final value of the nth triangular number
triangular = 0
# for loop that runs through 1-whichever n value we choose
for i in range(1, n + 1):
    # updating triangular by adding every value in the range
    triangular = triangular + i
# printing the nth triangular number we get from the for loop and
# throguh a formula n*(n+1)/2
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)

# Problem 4
# printing out header for problem 4
print("")
print("Problem 4 solution follows:")

# for loop to compute the 10 factorial
# setting n to the number we want the factorial of
n = 10
# variable factorial to hold final value n!
factorial = 1  # must be 1 not 0, 0 * anything is 0
# for loop that runs through n to 2 by subtracting 1 each time
# because multiplying by 1 dosnt matter
for i in range(n, 1, -1):
    # updating factorial by multiplying every value in the range
    factorial = factorial * i
# printing n!
print(str(n) + "!:", factorial)

# Problem 5
# printing out header for problem 5
print("")
print("Problem 5 solution follows:")

# variable holding how the first n factorials we want to calculate
num_lines = 10
# loop that will go through the first n factorials we want
# from highest to lowest
for i in range(num_lines, 0, -1):
    # nested for loop to calulate each factorial
    # same code from problem 4
    factorial = 1
    for j in range(i, 1, -1):
        factorial = factorial * j
    print(str(i) + "!:", factorial)

# Problem 6
# printing out header for problem 6
print("")
print("Problem 6 solution follows:")

# variable holding how many fractions (terms) to add
num_terms = 10
# starting value of e
e = 1
# for loop that runs thorough 1 to how many terms we want to add
for term in range(1, num_terms + 1):
    # variable to hold a temporary factorial value
    term_factorial = 1
    # nested for loop that will calculate a factorial of the "term" value
    for k in range(term, 1, -1):
        term_factorial = term_factorial * k  # updating temp factorial value
    # updating e by adding 1 divided by the term factorial value to e
    e = e + (1 / (term_factorial))
# printing out the value of e
print("e:", e)


# Collaboration
# no one
