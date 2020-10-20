import requests
from bs4 import BeautifulSoup as soup
import json

def fun(currency):
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
	r = requests.get(
	    "http://www.investing.com/currencies/Service/ChangeCurrency?session_uniq_id=517835a788eaf5bcc68a0a165cc24f82&currencies="+currency, headers=headers).text
	info = soup(r, 'lxml')
	li = info.find('script')
	for i in li:
		if i.string:
			i.string.replace_with(i.string.replace("\\",""))
	with open("d.html","w") as d:
		d.write(str(li))

	url = "d.html"
	page = open(url)
	s= soup(page.read(),'lxml')
	k = s.find_all('tr')
	lst = []

	for p_tag in k:
		try:
			if len(p_tag.findChildren()[4]['data-name']) == 7:
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