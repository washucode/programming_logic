def fizz_buzz(sum):
  
  
  if sum%3==0 and sum%5==0:
    return 'FizzBuzz'  
  
  elif sum%5==0:
    return 'Buzz'
  
  elif sum%3 ==0 :
    return 'Fizz'
  
  
  else:
    return sum
  