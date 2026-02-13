import requests as req
url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
res = req.get(url).text
print(res)
BTC_dollar = res[res.find("price")+8:res.find(".")]
KRW = 1448
money = str(int(BTC_dollar)*int(KRW))
print(money+"원")
print(money[0]+"억"+money[1:5]+"만"+money[5:]+"원")
won = str(int(BTC_dollar)*int(KRW))