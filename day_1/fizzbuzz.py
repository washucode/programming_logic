
#takes a num return FizzBuzz if divisble by both 3 and 5
#return Buzz if number if divisible by 5
#return Fizz if divisble by 3

def fizz_buzz(num):
  
  
  if num%3==0 and num%5==0:
    return 'FizzBuzz'  
  
  elif num%5==0:
    return 'Buzz'
  
  elif num%3 ==0 :
    return 'Fizz'
  
  
  else:
    return num
  