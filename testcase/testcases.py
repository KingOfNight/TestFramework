import requests
import json
import types

class shop():
    shopId=1    #店铺id
    shopName='shopname'  #店铺名
    managerShopId=43     #总店id
    openid = 'oWT18jmvvJ50Q-GhEPUeY0cgAp4U'
    def shop(self):

        return
    def set_shop_name(self,shopName):
        shopName=
        return
class testcases():
    def check_price(self):
        return
    def check_items(self):
        return
    def check_saleoff(self):
        return
    def check_memberoff(self):
        return

def get_dict_value(keyName,dictName):
    for key,val in dictName.items():
        print(key)
        if (key ==keyName):
            print(val)
            return val
        else:
            if(isinstance(val,dict)):
                get_dict_value(keyName,val)
    return

def compare_dict(dict1,dict2):

    return


def get_shop():
    shopUrl="http://qr-api.uat.9now.net/pay/api/shop.detail"
    #shopId=140375&tableId=101&tableNo=101&codeType=1&openid=oWT18jmvvJ50Q-GhEPUeY0cgAp4U&userid=39218614&fromw=2
    #shopData={'shopId':'140375','tableId':'101','tableNo':'101','codeType':'1','openid':'oWT18jmvvJ50Q-GhEPUeY0cgAp4U','userid':'39218614','fromw':'2'}
    shopData={'shopId':'140375','openid':'oWT18jmvvJ50Q-GhEPUeY0cgAp4U','fromw':'2'}
    headers={'Accept':'application/json'}
    try:
        shopInform=requests.post(shopUrl,data=shopData,headers=headers)
        shop=shopInform.json()
        isinstance(shop,dict)
    except BaseException:
        print("出现异常")
    else:
        print(shopInform.json())
    return -1

def get_order():
    shopId='140375'
    managerShopId='43'
    shopName='美味不用等(正大广场店)'
    thirdAccess='3'
    openid='oWT18jmvvJ50Q-GhEPUeY0cgAp4U'
    #code='6ie713nrt5e939'
    orderUrl="http://qr-api.uat.9now.net/pay/api/order.detail"
    headers = {'Accept': 'application/json'}
    orderData ={'shopId':shopId,'tableId':'001','tableNo':'001','managerShopId':managerShopId,'shopName':shopName,'thirdAccess':thirdAccess,'openid':openid}
    try:
        orderInform=requests.post(orderUrl,data=orderData,headers=headers)
    except BaseException:
        print("errors")
    else:
        print(orderInform.json())
    return orderInform.json()

def main():
    keyName='discountAmountPay'
    try:
        orderDict=get_order()
        discountAmountPayValue=get_dict_value(keyName,orderDict)
    except BaseException:
        print("error")
    else:
        print(discountAmountPayValue)
str=get_order()

get_dict_value('discountAmountPay',str)