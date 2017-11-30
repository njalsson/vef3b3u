from lxml import html
import requests



#my ethereum wallet
address = 'https://etherscan.io/address/0xe5c6daf760a1999ccc87afdb4c417d4f3097ccb0';


page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')


print('Buyers: ', buyers)
print('Prices: ', prices)
