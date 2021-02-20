import pandas as pd 
import numpy as np 
import requests

# class Stoxx:
#     def __init__(self, ticker, free_cred_access_key = "some_access_key_123", free_cred_access_secret = "some_access_secret_123"):
#         self.ticker = ticker
#         self.rapid_url = "www.someurl.com"
#         self.free_cred_access_key = "some_access_key_123"
#         self.free_cred_access_secret = "some_access_secret_123"
        
#     def get_company_data(self):
#         company_data = "https://cloud.iexapis.com/stable/stock/{ticker}/company?token=pk_8c5bd128eeab4bec97784baa1d133b30".format(ticker=self.ticker)
#         response = requests.get(company_data)
#         return response.json()

#     def get_company_ticker(self):
#         return self.ticker
    
#     def set_stoxx_keys(self, free_cred_access_key, free_cred_access_secret):
#         self.free_cred_access_key = free_cred_access_key
#         self.free_cred_access_secret = free_cred_access_secret

#     def get_stoxx_keys(self):
#         return self.free_cred_access_key, self.free_cred_access_secret

class Stoxx:
    def __init__(self):
        self.key = "some_access_key_123"
        self.secret = "some_access_secret_123"
        self.ticker = ""

    def get_key(self):
        return self.key

    def get_secret(self):
        return self.secret

    def RapidAPI(self, key, secret):
        self.key = key
        self.secret = secret

    def Ticker(self, ticker):
        self.ticker = ticker
        return self

    def get_company_data(self):
        company_data = "https://cloud.iexapis.com/stable/stock/{ticker}/company?token=pk_8c5bd128eeab4bec97784baa1d133b30".format(ticker=self.ticker)
        response = requests.get(company_data)
        return response.json()