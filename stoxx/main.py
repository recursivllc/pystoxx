# from stoxx import Stoxx
# aws_key = 1231343423
# aws_secret = 1231231242
# apple = Stoxx("appl")
# print(apple)
# print(apple.ticker)
# print(apple.get_company_data())
# print(apple.get_stoxx_keys())
# print(apple.set_stoxx_keys(aws_key, aws_secret))
# print(apple.get_stoxx_keys())

from stoxx import Stoxx
x_rapidapi_key = "5a62c537eemsh34406ef7e191f2fp150c91jsn02fafc190614"

stoxx = Stoxx()
print(stoxx.get_company_data(ticker="aapl"))
# print(Stoxx.get_key())
# print(Stoxx.get_secret())

stoxx.RapidAPI(x_rapidapi_key)

# print(Stoxx.get_key())
# print(Stoxx.get_secret())

# apple = Stoxx.Ticker("aapl")
# print("Apple: ", apple.ticker)
# print(apple.get_company_data(ticker="aapl"))
print(stoxx.get_company_data(ticker="aapl"))

print(stoxx.get_company_competition(ticker="aapl"))

print(stoxx.get_historical_news(ticker="aapl", months=1))

print(len(stoxx.get_public_companies()))

print(stoxx.calculate_sentiment("good news today!"))