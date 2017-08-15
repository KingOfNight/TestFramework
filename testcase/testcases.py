import requests
import json
import types

class shop():
    __shopId=1    #店铺id
    __shopName='shopname'  #店铺名
    __managerShopId=43     #总店id
    __openId = 'oWT18jmvvJ50Q-GhEPUeY0cgAp4U'
    tableNo='001'       #桌名
    tableId='001'       #桌号
    def __init__(self,shopId,shopName,managerShopId,openId):
        return

    #set properties
    def set_shopname(self,shopName):
        self.__shopName=shopName
        return
    def set_shopid(self,shopId):
        self.__shopId=shopId
        return
    def set_managershopid(self,managerShopId):
        self.__managerShopId=managerShopId
        return
    def set_openid(self,openId):
        self.__openId=openId
        return

    #get properties
    def get_shopid(self):
        return self.__shopId
    def get_shopname(self):
        return self.__shopName
    def get_managershopid(self):
        return
    def get_openid(self):
        return

class helper():
    thirdAccess = '3'       #连接方式3 为第三方餐饮系统
    def __init__(self):
        return

class testcases():

    mwshop=shop()
    def check_discount(self):
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