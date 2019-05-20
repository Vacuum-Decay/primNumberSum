import math

#Sums up all prime numbers up to limit 
def primeNumberSum(limit):
  #number is the number that is being checked whether to see if it is a prime
  number = 2
  #The variable being used to calculate the sum of all primes
  sum = 2
  #a list of all prime numbers
  primeNumberList = [2]
  

  while number < limit:
    number += 1 
    #Checks if the number being examined is prime
    isPrimeNumber = False
    #checks if number can be divided by all numbers in primeNumberList
    for primeNumber in primeNumberList:
      #if the number is divisible by a number in primeNumberList, then it is not a prime
      if number % primeNumber == 0:
        isPrimeNumber = False
        break
      #Otherwise, the number is a prime number. 
      else:
        isPrimeNumber = True
    if(isPrimeNumber == True):
      sum += number
      primeNumberList.append(number)
  print(sum)

primeNumberSum(3000)
