STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import json
import datetime
import news

class StockChecker:
    def __init__(self):

        self.today = datetime.date.today()
        self.today_str = str(self.today)
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.yesterday_str = str(self.yesterday)
        self.day_prior = self.yesterday - datetime.timedelta(days=1)
        self.day_prior_str = str(self.day_prior)
        self.day_name = self.today.strftime("%A")


    def check_stock(self, stock):
        self.stock = stock
        # alphavantage API
        API_KEY_ALPHAVANTAGE = "*****REDACTED KEY*******"
        PARAMS_ALPHAVANTAGE = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock,
            "interval": "60min",
            "apikey": API_KEY_ALPHAVANTAGE

        }



        if self.day_name == "Saturday":
            self.today -= datetime.timedelta(days=1)
            self.today_str = str(self.today)
            self.yesterday = self.today - datetime.timedelta(days=1)
            self.yesterday_str= str(self.yesterday)
            self.day_prior = self.yesterday - datetime.timedelta(days=1)
            self.day_prior_str = str(self.day_prior)
        elif self.day_name == "Sunday":
            self.today -= datetime.timedelta(days=2)
            self.today_str = str(self.today)
            self.yesterday = self.today - datetime.timedelta(days=1)
            self.yesterday_str = str(self.yesterday)
            self.day_prior = self.yesterday - datetime.timedelta(days=1)
            self.day_prior_str = str(self.day_prior)
        elif self.day_name == "Monday":
            # yesterday becomes last friday, day prior becomes last thursday
            self.today_str = str(self.today)
            self.yesterday = self.today - datetime.timedelta(days=3)
            self.yesterday_str = str(self.yesterday)
            self.day_prior = self.yesterday - datetime.timedelta(days=1)
            self.day_prior_str = str(self.day_prior)
        elif self.day_name == "Tuesday":
            # yesterday becomes monday, day prior becomes last friday
            self.today_str = str(self.today)
            self.yesterday = self.today - datetime.timedelta(days=1)
            self.yesterday_str = str(self.yesterday)
            self.day_prior = self.yesterday - datetime.timedelta(days=3)
            self.day_prior_str = str(self.day_prior)


        print(f"today_str: {self.today_str}")
        print(f"yesterday_str: {self.yesterday_str}")

        self.stock_response = requests.get(url="https://www.alphavantage.co/query", params=PARAMS_ALPHAVANTAGE)
        self.stock_response.raise_for_status()
        self.stock_response=self.stock_response.json()

        print(self.stock_response)

        print(self.stock_response["Time Series (Daily)"][self.today_str])
        print(self.stock_response["Time Series (Daily)"][self.yesterday_str])
        self.todays_open = float(self.stock_response["Time Series (Daily)"][self.today_str]["1. open"])
        self.yesterdays_open = float(self.stock_response["Time Series (Daily)"][self.yesterday_str]["1. open"])
        self.day_priors_open = float(self.stock_response["Time Series (Daily)"][self.day_prior_str]["1. open"])

        print(f"Today's open: {self.todays_open}")
        print(f"Yesterday's open: {self.yesterdays_open}")
        print(f"Day Prior to yesterday's open: {self.day_priors_open}")
        self.stock_change()

    def stock_change(self):
        self.percent_change = ((self.yesterdays_open-self.day_priors_open)/self.day_priors_open)*100
        return self.percent_change
