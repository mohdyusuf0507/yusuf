def isleapyear(year):
  if (year % 4 == 0 and year % 100 !=0 ) or year % 400 == 0:
    return True
  else:
    return False

year = int(input("enter a value : "))

if isleapyear(year):
  print('{} is a leapyear.'.format(year))
else:
  print('{} is a not a leap year.'.format(year))