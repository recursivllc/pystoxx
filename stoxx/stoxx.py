import pandas as pd 
import numpy as np 
import requests
import json

class Stoxx:
    def __init__(self):
        self.x_rapidapi_key = ""
        self.x_rapidapi_host = "stoxx-by-recursiv.p.rapidapi.com"

    def get_key(self):
        return self.x_rapidapi_key

    def get_secret(self):
        return self.secret

    def RapidAPI(self, x_rapidapi_key):
        self.x_rapidapi_key = x_rapidapi_key
        self.x_rapidapi_host = "stoxx-by-recursiv.p.rapidapi.com"

    def get_company_data(self, ticker):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/company/{ticker}/info".format(ticker=ticker)
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_company_competition(self, ticker):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/company/{ticker}/competition".format(ticker=ticker)
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_historical_news(self, ticker, months):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/company/{ticker}/history/{months}".format(ticker=ticker,months=months)
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_public_companies(self):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/companies"
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_historical_prices(self, ticker, range):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/company/{ticker}/prices/{range}".format(ticker=ticker,range=range)
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_company_quote(self, ticker):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/company/{ticker}/quote".format(ticker=ticker)
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def calculate_sentiment(self, text):
        url = "https://stoxx-by-recursiv.p.rapidapi.com/api/v1/stoxx/calculate/sentiment"
        payload = json.dumps({"content" : "This is a wonderful and amazing API!"})
        headers = {
            'content-type': "application/json",
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()