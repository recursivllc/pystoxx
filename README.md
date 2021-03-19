# PyStoxx: 

<p align="center">
  <img src="https://github.com/recursivllc/external-facing-images/blob/master/stoxx/stoxxByRecursiv_blue.png?raw=true" width="100" alt="accessibility text">
</p>


PyStoxx is a Python library of [Stoxx by Recursiv](https://recursiv.tech/) that allows users to retrieve current data and historical information for publicly traded companies with our JSON API.

## Features Include:
- Current & Historical Company Sentiment
- Company News Articles
- Pricing History
- Price Quotes
- Company Data
- Company Competition

## Quick Start Guide

1. Install Stoxx using Pip

        pip install pystoxx

2. Import Stoxx

        from pystoxx import Stoxx

3. Add your API Token using the RapidAPI extension. Sign up for a free plan without a credit card by visiting [Stoxx By Recursiv hosted at RapidAPI.](https://rapidapi.com/recursivllc/api/stoxx-by-recursiv)

        stoxx = Stoxx()
        stoxx.RapidAPI("add-your-token-here")

4. Query your data of interest:

        ​stoxx.get_historical_prices(ticker="msft", months=2)

## Query Current and Historical Stock Ticker Data:

### Historical Pricing Data:

Input:

        # Get historical daily pricing data
        stoxx.get_historical_prices(ticker="msft", months=2)

Output:

        {
        "changePercent": 0,
        "close": 198.76,
        "date": "2020-03-19",
        "high": 208.75,
        "low": 195.27,
        "open": 201,
        "symbol": "MSFT",
        "updated": 1613017108000,
        "volume": 4796717
        }

### Historical News & Sentiment Data:

Input:

        # Get historical news & sentiment data
        stoxx.get_historical_news(ticker="msft", months=2)

Output:

        {
        "FeedUrl": "url-to-article",
        "Polarity": 0.08882323,
        "PublishDate": "2021-02-17T20:04:00+00:00",
        "Subjectivity": 0.2944154,
        "Title": "News Corp. and Google Settle Long Pay Fight With Global News Pact",
        "VaderAggregate": 0.9933,
        "VaderNegative": 0.045,
        "VaderNeutral": 0.827,
        "VaderPositive": 0.127,
        "id": "4cb8b419-2ec1-32d0-849a-2ac524475c23"
        },

### Company Data and Information:

Input:

        # Get company information
        stoxx.get_company_data("msft")

Output:

        {
                "companyName": "Microsoft Corporation",
                "country": "US",
                "industry": "Data Processing, Hosting, and Related Services",
                "sector": "Information",
                "symbol": "MSFT",
                "tags": [
                "Technology Services",
                "Packaged Software",
                "Information",
                ],
                "website": "https://www.microsoft.com/en-us",
                "zip": "98052-6399"
        }

### Stock Ticker Price Quote:

Input:

        # Get a price quote
        stoxx.get_price_quote("msft")

Output:

        {
                "close": 230.72,
                "exchange": "NASDAQ/NGS (GLOBAL SELECT MARKET)",
                "high": 234.19,
                "high52w": 245.56,
                "lastTime": "March 18, 2021",
                "lastUpdate": 1616097600583,
                "low": 230.33,
                "low52w": 131.19,
                "marketCap": 1740140021762,
                "name": "Microsoft Corporation",
                "pe": 34.38,
                "symbol": "MSFT",
                "volume": 34852251
        }

### List of Publicly Traded Company Tickers:

Input:

        # Get a list of all publicly traded companies
        stoxx.get_public_companies()

Output:

        [
                { "symbol" : "msft" },
                { "symbol" : "amzn" },
                { "symbol" : "amgn" },
                ...
        ]

### Find Company Competition:

Input:

        # Get company competition
        stoxx.get_company_competition("msft")

Output:

        {
        "company": "msft",
        "competition": [
                "ORCL",
                "IBM",
                "GOOGL",
                "AAPL",
                ...
        ]
        }

### Get Current Market Performance by Sector:

Input:

        # Get market performance
        stoxx.get_market_performance()

Output:

        [
                {
                "datetimeUpdated": 1616097600045,
                "performance": -0.00209,
                "sector": "Health Care"
                },
                ...
        ]

### Calculate Sentiment of Stock Market Text:

Input:

        # Calculate Sentiment
        stoxx.calculate_sentiment({"content" : "This is an amazing pypi library!"})

Output:

        {
                "VaderPositive": 0.45,
                "VaderNeutral": 0.55,
                "VaderNegative": 0.0,
                "VaderAggregate": 0.6239,
                "Subjectivity": 0.9,
                "Polarity": 0.750
        }










