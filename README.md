# Investing.com-Webscraper
This is a web scraper for investing.com/currencies/single-currency-crosses on the site investing.com

## NOTE:
    INSERT THE ID PARAMETER IN BOTH THE FILES BY FINDING YOU'RE PHP UNIQUE SESSION ID IN functions.py
    ALSO CREATE YOU'RE MONGO DB AND CONNECT IT IN functions.py

In this we are going to start a web server using flask and with this we are able to use the server on our local host and use this program as an API and make these calls to get the input from the user if required.

## There are three main files which are being used:
    1.functions.py
    2.web.py
    3.always.py

1. functions.py -> This has all the functions for both the insertion and the searching of the data files, thus this is the major code file of our program. I've implemented the data for a certain number of currencies which i needed and then am making the updates for those currencies only.I've implemented multi threading as well to reduces the time for the scrapping.


2. web.py -> Now coming to the main part when we will go to the /[id] and this is the file which sets up the server for the user and then helps them access the whole data
In this we are supposed to give out the id of the currency we want to display on our page.

3. always.py -> This a basic while loop in which we are updating the database for all the data and thus giving the user live data which is being scrapped and updated locally thus improving the speed

## Logic behinde the working of the program:
The site loads dynamically and makes use of the request to this page 

    /currencies/Service/ChangeCurrency?session_uniq_id=[value]&currencies=[currency_id]

which return the data and then the data is inserted on the investing.com/currencies/single-currency-crosses page.
The request which is being made is

![alt text](https://github.com/TanishqChamoli/Investing.com-Webscraper/blob/main/Images/Request.jpg)

So what I'm doing is asking for the session id from the user and the currency id, thus returning the data for that currency in a json format.
Thus giving us the output as

![alt text](https://github.com/TanishqChamoli/Investing.com-Webscraper/blob/main/Images/Output.png)


Author Tanishq Chamoli
