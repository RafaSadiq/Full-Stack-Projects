# function
# looping
# conditionals
# math operators

# Write a program that prints the numbers from 1 to infinity. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "buzz". For numbers which are multiples of both three and five print "FizzBuzz".

def multiples(num):
    for number in range(1, num + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)
            
multiples(100)
    
