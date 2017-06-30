import requests
import json

class test:
    def __init__(self):
        return
    def importData(self):
        return
    def cleanData(self):
        return

class testcases:
    def testpot(self):
        s=[{'shopid':12,'fromw':2}]
        j=json.dump(s)
        # shopid int 店铺id; openid string openid; fromw int 1app 2微信 3支付宝
        r=requests.post(" http://qr-st.api.9now.net/",j)
        return
    def check_price(self):
        return
    def check_items(self):
        return
    def check_saleoff(self):
        return
    def check_memberoff(self):
        return