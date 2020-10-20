# Investing.com-Webscraper
This is a web scraper for investing.com/currencies/single-currency-crosses on the site investing.com

## NOTE:
    INSERT THE ID PARAMETER IN BOTH THE FILES BY FINDING YOU'RE PHP UNIQUE SESSION ID

In this we are going to start a web server using flask and with this we are able to use the server on our local host and use this program as an API and make these calls to get the input from the user if required.

## There are three main files which are being used:
    1.ape.py
    2.para_scrape.py
    3.web.py

1. ape.py -> This will scrape all the data from investing.com/currencies/single-currency-crosses with CHF as the parameter of the search.
This is for the proof of concept that we can extract the data ad many times as we want using this scraper and will return the
live data from the website as well.


2. para_scrcape.py -> Now coming to the main part when we will go to the /new/[id]
In this we are supposed to give out the id of the currency we want to display on our page.

3.web.py -> this contains the flask program which is needed to make this as an api call rather than giving an terminal output.

## Logic behinde the working of the program:
The site loads dynamically and makes use of the request to this page 
/currencies/Service/ChangeCurrency?session_uniq_id=[value]&currencies=[currency_id]
which return the data and then the data is inserted on the 
investing.com/currencies/single-currency-crosses page.
The request which is being made is

![alt text](https://github.com/TanishqChamoli/Investing.com-Webscraper/blob/main/Images/Request.jpg)

So what I'm doing is asking for the session id from the user and the currency id, thus returning the data for that currency in a json format.
Thus giving us the output as

![alt text](https://github.com/TanishqChamoli/Investing.com-Webscraper/blob/main/Images/Output.png)


Author Tanishq Chamoli
