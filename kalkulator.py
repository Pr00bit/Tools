 
print (' -------------Witaj w kalkulatorze------------by pr0bit')
print ('                dodawanie')
print ('                odejmowanie')
print ('                mnozenie')
print ('                odejmowanie')
 

 
name   = int(input('co chcesz robic: '))   #int ma byc bo domyslnie input jest stringiem
if name == 1:
   pierwsza = int(input('Ppodaj pierwsza liczbe'))
   druga = int(input ('Ppodaj druga liczbe'))       
   c = pierwsza + druga
   print (c)
elif name == 2:
   pierwsza = int(input('Ppodaj pierwsza liczbe'))
   druga = int(input ('Ppodaj druga liczbe'))       
   c = pierwsza - druga
   print (c)
elif name == 3:
   pierwsza = int(input('Ppodaj pierwsza liczbe'))
   druga = int(input ('Ppodaj druga liczbe'))       
   c = pierwsza * druga
   print (c)
elif name == 4:
   pierwsza = int(input('Ppodaj pierwsza liczbe'))
   druga = int(input ('Ppodaj druga liczbe'))       
   c = pierwsza / druga
   print (c)
 
 
dalej=  input('czy chcesz dalej uzywac T/N')
a