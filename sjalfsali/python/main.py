import json       # to use json
import requests   # easy library to get data from port 80
import time       # make it run once a second
import RPi.GPIO as GPIO
import motor.py 
from time import sleep


#my ethereum wallet
address = 'http://api.etherscan.io/api?module=account&action=txlist&address=0xe5c6daf760a1999ccc87afdb4c417d4f3097ccb0&startblock=0&endblock=99999999&sort=asc&apikey=YGSWPV6U2U34VMFFS3C5EMSXXMPPZS2DR1B'

r = requests.get(address)

print(r.status_code) # works?




json = r.json() # convert json to python dictionary

i = 0 # figure out how many payments there have been made to a specific account.
for x in json['result']: # i - 1 is the last payment.
	i += 1

print(i) # debug, todo: remove
print(json['result'][i-1]['hash']) # get the latest hash of payment, i thing this is unique, what ever

last = json['result'][i-1]['hash']

while True: # basically run once a second to see if latest hash changed.
        del r # save precious ram space.
        del json
        del i
        r = requests.get(address) # redownload
        json = r.json()
        i = 0
        for x in json['result']:
                i += 1

        lastbutnotleast = json['result'][i-1]['hash']

        if lastbutnotleast != last:
                last = lastbutnotleast
                print('payment received')
                motor.start()
                motor.angle(180)
                os.sleep(1)
                motor.angle(90)
                motor.stop()
                ## todo run vending machine.



