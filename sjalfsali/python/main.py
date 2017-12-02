import json
import requests



#my ethereum wallet
address = 'http://api.etherscan.io/api?module=account&action=txlist&address=0xe5c6daf760a1999ccc87afdb4c417d4f3097ccb0&startblock=0&endblock=99999999&sort=asc&apikey=YGSWPV6U2U34VMFFS3C5EMSXXMPPZS2DR1B'

r = requests.get(address)

print(r.status_code)




json = r.json()

i = 0
for x in json['result']:
	i += 1

print(i)
print(json['result'][i-1]['hash'])

last = json['result'][i-1]['hash']

while True:
        del r
        del json
        del i
        r = request.get(address)
        json = r.json()
        i = 0
        for x in json['result']:
                i += 1

        
        lastbutnotleast = json['result'][i-1]['hash']

        if lastbutnotleast != last:
                lastbutnotleast = last
                print('payment received')

                ## todo run thing



        
