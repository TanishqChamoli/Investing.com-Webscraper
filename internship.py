import requests
from bs4 import BeautifulSoup as soup
import json

def fun():
	headers = {
	    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
	    "Accept": "application/json, text/javascript, */*; q=0.01",
	    "Accept-Language": "en-US,en;q=0.5",
	    "Accept-Encoding": "gzip, deflate",
	    "Connection": "close",
	    "Host": "www.investing.com",
	    "Upgrade-Insecure-Requests": "1",
	    "Referer": "https://www.investing.com/currencies/single-currency-crosses",
	    "X-Requested-With": "XMLHttpRequest",
	}
	id = "" #this is supposed to be inserted
	r = requests.get(
	    "http://www.investing.com/currencies/Service/ChangeCurrency?session_uniq_id="+id+"&currencies=4", headers=headers).text
	info = soup(r, 'lxml')
	li = info.find('script')
	for i in li:
		if i.string:
			i.string.replace_with(i.string.replace("\\",""))
	with open("d.html","w") as d:
		d.write(str(li))

	url = "d.html"
	ar = ['USD/CHF', 'CHF/USD', 'EUR/CHF', 'CHF/EUR', 'CHF/JPY', 'JPY/CHF', 'GBP/CHF', 'CHF/GBP', 'AUD/CHF', 'CHF/AUD', 'CAD/CHF', 'CHF/CAD', 'CHF/SEK', 'SEK/CHF', 'NZD/CHF', 'CHF/NZD', 'CHF/INR']
	page = open(url)
	pids = ['4', '10', '12', '13', '14', '48', '57', '86', '90', '107', '108', '113', '123', '126', '136', '138', '140', '1508', '1540', '1541', '1542', '1543', '1544', '1545', '1546', '1547', '1548', '1549', '1550', '1551', '1553', '1554', '1555', '1556', '1558', '1559', '1560', '1582', '1880', '1892', '1973', '2015', '2029', '2063', '9279', '9333', '9495', '9541', '9542', '9543', '9546', '9547', '9548', '9549', '9550', '9551', '9552', '9555', '9556', '9557', '9558', '9559', '9560', '9561', '9562', '9563', '9564', '9565', '9566', '9567', '9568', '9619', '9680', '9794', '9978', '10076', '10302', '10352', '10409', '13918', '13927', '53088', '940803', '993163', '993164', '1031292', '1089812']

	s= soup(page.read(),'lxml')
	k = s.find_all('tr')
	lst = []

	for p_tag in k:
		try:
			if len(p_tag.findChildren()[4]['data-name']) == 7 and p_tag.findChildren()[4]['data-name'] in ar:
				dic = {}
				dic['data-name'] = p_tag.findChildren()[4]['data-name']
				dic['bid'] = p_tag.findChildren()[5].text
				dic['ask'] = p_tag.findChildren()[6].text
				dic['high'] = p_tag.findChildren()[7].text
				dic['low'] = p_tag.findChildren()[8].text
				dic['change'] = p_tag.findChildren()[9].text
				dic['change %'] = p_tag.findChildren()[10].text
				dic['date'] = p_tag.findChildren()[11]['data-value']
				dic['time'] = p_tag.findChildren()[11].text
				lst.append(dic)
		except:
			pass
	# j= json.dumps(lst)
	return lst