STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import json
import datetime
from stocks import StockChecker
import newsapi
import news
import sms


stock_data = StockChecker()
stock_data.check_stock(stock=STOCK)
stock_change = stock_data.stock_change()
print(stock_change)

news_parameters = {
    "apiKey": "********REDACTED KEY*******",
    "q": COMPANY_NAME,
    "domains": "bbc.com, npr.org, npr.com, reuters.com, marketwatch.com",
    "from": "7-28-2022"


}

if abs(stock_change) >= 5:
    if (stock_change) > 0:
        price_change = "up 🔺"
    elif (stock_change) < 0:
        price_change = "down 🔻"
    news_check = news.NewsChecker()
    news_list = news_check.check_news(news_param = news_parameters)
    print(news_list)

    # Now call the sms feature
    message = f"{STOCK} {price_change}{round(stock_change,2)}%\n\n" \
              f"{news_list[0]['title']}\n" \
              f"{news_list[0]['description']}\n" \
              f"{news_list[0]['URL']} \n\n" \
              f"{news_list[1]['title']}\n" \
              f"{news_list[1]['description']}\n" \
              f"{news_list[1]['URL']} \n\n" \
              f"{news_list[2]['title']}\n" \
              f"{news_list[2]['description']}\n" \
              f"{news_list[2]['URL']} \n\n"
    sms.send_alert(body=message)
else:
    pass

