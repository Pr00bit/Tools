
import requests

cookies = dict(WC='11016446-16730-fffffff') #cookie of we chall from my pc
r = requests.get('http://www.wechall.net/challenge/training/programming1/index.php?action=request', cookies=cookies) #coolies needs to bend for authorisation
z= r.text


r = requests.get('http://www.wechall.net/challenge/training/programming1/index.php?answer='+z, cookies=cookies)

