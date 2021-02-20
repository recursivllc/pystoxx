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
aws_key = "1231343423"
aws_secret = "1231231242"

Stoxx = Stoxx()

# print(Stoxx.get_key())
# print(Stoxx.get_secret())

Stoxx.RapidAPI(aws_key, aws_secret) #Working

# print(Stoxx.get_key())
# print(Stoxx.get_secret())

apple = Stoxx.Ticker("aapl")
print("Apple: ", apple.ticker)
print(apple.get_company_data())

amgen = Stoxx.Ticker("amgn")
print("Amgen: ", amgen.ticker)
print(amgen.get_company_data())

wayfair = Stoxx.Ticker("w")
print("Amgen: ", amgen.ticker)
print(wayfair.get_company_data())