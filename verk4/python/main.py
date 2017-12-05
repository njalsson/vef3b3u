import json           # to use json
import requests       # easy library to get data from port 80
import time           # make it run once a second
import tkinter as tk  # the window framework
from tkinter import *
from tkinter import ttk
import random
import threading

#my ethereum wallet
address = 'http://api.etherscan.io/api?module=account&action=txlist&address=0xe5c6daf760a1999ccc87afdb4c417d4f3097ccb0&startblock=0&endblock=99999999&sort=asc&apikey=YGSWPV6U2U34VMFFS3C5EMSXXMPPZS2DR1B'

r = requests.get(address)

print(r.status_code)  # works? if 200


compliments = [
		'þú með fallegt hár!',
		'Jón Gnarr er ljótur hliðina á þér',
		'hallo heimur',
		'Nenni ekki að gera fleiri hrós.!',
]

json = r.json() # convert json to python dictionary

i = 0 # figure out how many payments there have been made to a specific account.
for x in json['result']: # i - 1 is the last payment.
	i += 1

print(i) # debug, todo: remove
print(json['result'][i-1]['hash'])  # get the latest hash of payment, i thing this is unique, what ever

last = json['result'][i-1]['hash']





###############################
# setting up tkinter gui      #
###############################
# then when you get payment it updates the text to a random compliment
# and the address


root = tk.Tk()

root.title("Verkefni 4")

frame = Frame(root)

logo = logo = tk.PhotoImage(file="../images/ethereum.png")


w1 = tk.Label(root, image=logo).pack(side="right")

nr1 = "new payment was from {}".format(json['result'][i-1]['from'])

## getting a random compliment from array
nr2 = compliments[random.randint(0,len(compliments)-1)]
w1 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 0, 
              text=nr1,
              font = "Helvetica 12 bold italic")

w1.pack(side="top")
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=nr2,
              font = "Helvetica 16 bold italic")
w2.pack(side="bottom")











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
		#print "amount", json['result'][i-1]['amount']
		root.update()
		if lastbutnotleast != last:
				last = lastbutnotleast
				print('payment received')
				## todo run vending machine.
				# put the transaction account and the amount in ethereum and in usd to the tkinter program
				newcomliment = compliments[random.randint(0,len(compliments)-1)]
				newtextnr1 = "new payment from {}: ".format(last)
				w1.destroy()
				w2.destroy()	
				w1 = tk.Label(root, 
								justify=tk.LEFT,
								padx = 0, 
								text=nr1,
								font = "Helvetica 12 bold italic").pack(side="top")
				w2 = tk.Label(root, 
								justify=tk.LEFT,
								padx = 10, 
								text=nr2,
								font = "Helvetica 16 bold italic").pack(side="bottom")


