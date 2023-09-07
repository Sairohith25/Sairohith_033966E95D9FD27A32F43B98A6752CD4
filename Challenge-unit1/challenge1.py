def factorial(x):
  if x == 0:
    return 1
  else:
    return x* factorial(x-1)

x=6
res = factorial(x)
print("The factorial of {} is {}".format(x,res))