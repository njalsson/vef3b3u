import json
import requests



#my ethereum wallet
address = 'http://api.etherscan.io/api?module=account&action=txlist&address=0xe5c6daf760a1999ccc87afdb4c417d4f3097ccb0&startblock=0&endblock=99999999&sort=asc&apikey=YGSWPV6U2U34VMFFS3C5EMSXXMPPZS2DR1B'

r = requests.get(address)

print(r.status_code)




json = r.json()
print(json)



for x in json['result'][0]:
	print(x)