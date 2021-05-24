import requests
from bs4 import BeautifulSoup as soup
import json
import pymongo
from pymongo import MongoClient
from multiprocessing.dummy import Pool as ThreadPool
import time

client = pymongo.MongoClient("mongodb+srv://tanishq:tanishq@live-stock.nyuyi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['currency']
collection = db['currency']

curr_name = {'22':'AED','32':'ARS','1':'AUD','59':'BDT','37':'BND','35':'BRL','38':'BSD','15':'CAD','4':'CHF','17':'EUR','3':'GBP','20':'HKD','23':'ILS','29':'INR','56':'IQD','2':'JPY','115':'LKR','14':'MXN','129':'NPR','5':'NZD','75':'PKR','76':'QAR','79':'RUB','18':'SEK','19':'SGD','9':'TRY','12':'USD'}

def fun(currency):
    try:
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
            "http://www.investing.com/currencies/Service/ChangeCurrency?session_uniq_id=[session-id]="+currency, headers=headers).text
        info = soup(r, 'lxml')
        li = info.find('script')
        for i in li:
            if i.string:
                i.string.replace_with(i.string.replace("\\",""))
        s = soup(str(li),'lxml')
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
        insert_mongo(lst,currency)
    except Exception as e:
        print(e)

def insert_mongo(data,currency):
    f_data = {}
    f_data['currency'] = currency
    f_data['data'] = data
    f_data['name'] = curr_name[currency]
    try:
        # collection.insert_one(f_data)
        collection.update_one({"currency":currency},{"$set":{'data':f_data['data']}})
        return True
    except Exception as e:
        print(e)
        return False

def get_data(currency):
    temp = list(collection.find({'currency':currency},{'_id':0}))
    return temp

def loop():
	currencies = ['22','32','1','59','37','35','38','15','4','17','3','20','23','29','56','2','115','14','129','5','75','76','79','18','19','9','12']
	start = time.time()
	pool = ThreadPool(10)
	pool.map(fun, currencies)
	pool.close()
	pool.join()
	end = time.time()

if __name__ == '__main__':
	while(1):
		loop()
		print(get_data("12"))
		time.sleep(2)
