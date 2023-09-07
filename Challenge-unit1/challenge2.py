year = int(input("Enter the leap year:"))
if (year %4==0) and (year %100!=0):
  print("{} is a leap year".format(year))
elif (year %100==0) and (year %4==0):
  print("{} is a leap year".format(year))
else:
  print("{} is not a leap year".format(year))