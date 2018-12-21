#Tool to search pages in Google, program will ask for fraze to search
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

  
# to search
while True:  #endless loop
  name = input("your fraze for Google to search:")
  query = name
  for j in search(query, tld="pl", num=30, stop=1, pause=2): 
    print(j) 
