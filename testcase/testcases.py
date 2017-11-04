import requests
import json
import types
import unittest

class testShop():
    shopId=1    #店铺id
    shopName='shopname'  #店铺名
    managerShopId=43     #总店id
    openId = 'oWT18jmvvJ50Q-GhEPUeY0cgAp4U'
    tableNo='001'       #桌名
    tableId='001'       #桌号
    shopUrl = "http://qr-api.uat.9now.net/pay/api/shop.detail"      #获取店铺信息
    orderUrl = "http://qr-api.uat.9now.net/pay/api/order.detail"        #获取订单信息

    headers = {'Accept': 'application/json'}
    thirdAccess = '3'  # 连接方式3 为第三方餐饮系统

    def __init__(self):
        return

    def __init__(self,shopId,shopName,managerShopId,openId):
        self.shopId=shopId
        self.shopName=shopName
        self.managerShopId=managerShopId
        self.openId=openId
        return
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
    def get_shop(self):
        shopUrl = "http://qr-api.uat.9now.net/pay/api/shop.detail"
        # shopId=140375&tableId=101&tableNo=101&codeType=1&openid=oWT18jmvvJ50Q-GhEPUeY0cgAp4U&userid=39218614&fromw=2
        # shopData={'shopId':'140375','tableId':'101','tableNo':'101','codeType':'1','openid':'oWT18jmvvJ50Q-GhEPUeY0cgAp4U','userid':'39218614','fromw':'2'}
        shopData = {'shopId': '140375', 'openid': 'oWT18jmvvJ50Q-GhEPUeY0cgAp4U', 'fromw': '2'}
        headers = {'Accept': 'application/json'}
        try:
            shopInform = requests.post(shopUrl, data=shopData, headers=headers)
            shop = shopInform.json()
            isinstance(shop, dict)
        except BaseException:
            print("出现异常")
        else:
            print(shopInform.json())
        return

    def get_order(self,tableId,tableNo):
        orderData = {'shopId': self.shopId, 'tableId': tableId, 'tableNo':tableNo, 'managerShopId':self.managerShopId,
                     'shopName': self.shopName, 'thirdAccess': self.thirdAccess, 'openid': self.openId}
        try:
            orderInform = requests.post(self.orderUrl, data=orderData, headers=self.headers)
            orderInform.status_code
        except:
            print("connect error!")
        return orderInform.json()
    def make_order(self):
        return

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
    '''def get_dict_value(self,keyName, dictName):
        for key, val in dictName.items():
            print(key)
            if (key == keyName):
                print(val)
                return val
            else:
                if (isinstance(val, dict)):
                    self.get_dict_value(keyName, val)
        return '''''

class testCaseSetup(testShop):
    def __init__(self):
        return
    def setup(self):
        return
    def cleanup(self):
        return

#智慧餐饮系统
class zhiHuiTestCases(testCaseSetup):
    tip=10
    #校验服务费
    def check_tips(self,tip):
        tableId='002'
        tableName='002'
        orderJs=helper
        value=''
        ordertip=orderJs.get_dict_value(value,self.get_order(tableId,tableName))
        if(orderJs):
            if (tip ==ordertip):
                return
        else:
            print('应收服务费与拉取服务费不同')
            return

    def check_mutiSetMeal(self,):
        return

#博优3.1
class boYouTestCases(testCaseSetup):
    tableDict={}
    def __init__(self):
        self.setup(self.softwareName)
        return
    def normal_dishes(self):
        self.get_order()
        return
    pass

#天财商龙
class tianCaiShangLongTestCases(testCaseSetup):
    def normal_dishes(self):
        tableId='001'
        tableNo='001'
        expectInfo={'dishname':'普通菜','price':10}
        orderInfo=self.get_order(tableId,tableNo)
        s=helper.get_dict_value('goods',orderInfo)
        print(s)
        return
    pass

class FlashPay(unittest.TestCase):
    def test_normal_dishes(self):
        return 
    pass


