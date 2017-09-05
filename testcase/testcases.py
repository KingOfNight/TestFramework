import requests
import json
import types

class testShop():
    shopId=1    #店铺id
    shopName='shopname'  #店铺名
    managerShopId=43     #总店id
    openId = 'oWT18jmvvJ50Q-GhEPUeY0cgAp4U'
    tableNo='001'       #桌名
    tableId='001'       #桌号
    orderUrl = "http://qr-api.uat.9now.net/pay/api/order.detail"
    headers = {'Accept': 'application/json'}
    thirdAccess = '3'  # 连接方式3 为第三方餐饮系统

    def __init__(self,shopId,shopName,managerShopId,openId):
        self.shopId=shopId
        self.shopName=shopName
        self.managerShopId=managerShopId
        self.openId=openId
        return

    @property.setter
    def set_shopname(self,shopName):
        self.shopName=shopName
        return
    def set_shopid(self,shopId):
        self.shopId=shopId
        return
    def set_managershopid(self,managerShopId):
        self.managerShopId=managerShopId
        return
    def set_openid(self,openId):
        self.openId=openId
        return
    def set_tableNo(self,tableNo):
        self.tableNo=tableNo
        return
    def set_tableId(self,tableId):
        self.tableId=tableId
        return

    @property.getter
    def get_shopid(self):
        return self.shopId
    def get_shopname(self):
        return self.shopName
    def get_managershopid(self):
        return self.managerShopId
    def get_openid(self):
        return self.openId
    def get_tableNo(self):
        return self.tableNo
    def get_tableId(self):
        return self.tableId

    @classmethod
    def get_order(self,shopId,tableId,tableNo,managerShopId,shopName,thirdAccess,openId):
        orderData = {'shopId': shopId, 'tableId': tableId, 'tableNo':tableNo, 'managerShopId': managerShopId,
                     'shopName': shopName, 'thirdAccess': thirdAccess, 'openid': openId}
        try:
            orderInform = requests.post(self.orderUrl, data=orderData, headers=self.headers)
            orderInform.status_code
        except:
            print("connect error!")
        return orderInform.json()


class helper():
    def __init__(self):
        return
    def check_orderinform(self):
        return
    def check_discount(self):
        return
    def check_items(self):
        return
    def check_saleoff(self):
        return
    def check_memberoff(self):
        return
    def check_order_two_onsale_dishes(self):
        return
    def compare_dict(correctData,getData):
        correctData
        return

    #获取字典中某一属性的值
    def get_dict_value(self,keyName, dictName):
        for key, val in dictName.items():
            print(key)
            if (key == keyName):
                print(val)
                return val
            else:
                if (isinstance(val, dict)):
                    self.get_dict_value(keyName, val)
        return False

class testCaseSetup():
    def __init__(self):
        return
    mwshop=testShop()
    def setup(self):
        return
    def cleanup(self):
        return


class boYouTestCase(testCaseSetup):
    softwareName='博优'
    tableDict={}
    def __init__(self):
        self.setup(self.softwareName)
        return
    def normal_dishes(self):
        self.ge
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
    return


