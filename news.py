import newsapi
import requests

class NewsChecker:

    def __init__(self):
        pass

    def check_news(self, news_param):

        self.news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_param)
        self.news_response.raise_for_status()
        self.news_response = self.news_response.json()
        print(self.news_response)
        self.article_one = {}
        self.article_one.update({"title": self.news_response["articles"][0]["title"]})
        self.article_one.update({"description": self.news_response["articles"][0]["description"]})
        self.article_one.update({"URL": self.news_response["articles"][0]["url"]})

        self.article_two = {}
        self.article_two.update({"title" : self.news_response["articles"][1]["title"]})
        self.article_two.update({"description": self.news_response["articles"][1]["description"]})
        self.article_two.update({"URL": self.news_response["articles"][1]["url"]})

        self.article_three = {}
        self.article_three.update({"title": self.news_response["articles"][2]["title"]})
        self.article_three.update({"description": self.news_response["articles"][2]["description"]})
        self.article_three.update({"URL" :self.news_response["articles"][2]["url"]})

        self.article_list = [self.article_one, self.article_two, self.article_three]

        return self.article_list
