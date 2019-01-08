def get_fib(position):
  
  if position == 0: return 0
  if position == 1: return 1
  first = 0
  second = 1
  next_ = first + second

  for i in range(2,  position):
    first = second
    second = next_
    next_ = first + second
  
  return next_

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)