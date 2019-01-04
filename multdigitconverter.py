# tool to convert digits by pr0bit


print (' Choose action you would like to take')
print ('1. convert decymal to hexadymal')

y = int(input('your chooise: '))


if y == 1:
   print (' Type in digit for conversion')
   x = int(input('your decimal number: '))
   if x < 256:
           print(' your number is less then 256')

else:
    print('wrong number')
