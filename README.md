# PyStoxx:

PyStoxx is a Python library of [Stoxx by Recursiv](https://recursiv.tech/) that allows users to retrieve current data and historical information for publicly traded companies with our JSON API.

#### Features Include:
- Current & Historical Sentiment
- News Articles
- Pricing History
- Price Quotes
- Company Data
- Company Competition

#### Quick Start Guide

1. Install Stoxx using Pip

        pip install pystoxx

2. Import Stoxx

        from pystoxx import Stoxx

3. Add your API Token using the RapidAPI extension. Sign up for a free plan without a credit card by visiting [Stoxx By Recursiv hosted at RapidAPI.](https://rapidapi.com/recursivllc/api/stoxx-by-recursiv)

        stoxx = Stoxx()
        stoxx.RapidAPI("add-your-token-here")

4. Query pricing data, historical news, and much more!


        # Get historical pricing data
        stoxx.get_historical_prices(ticker="msft", months="1m")

        # Get historical pricing data
        stoxx.get_historical_news(ticker="msft", months=2)

        # Get historical pricing data
        stoxx.get_company_data("msft")

        # Get price quote
        stoxx.get_price_quote("msft")



