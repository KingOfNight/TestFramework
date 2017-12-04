import requests
import json
import types
import unittest
import re

class testShop():
    shopId=140375    #店铺id
    shopName='美味不用等(正大广场店)'  #店铺名
    managerShopId=43     #总店id
    openId = 'oi_f8t_w4w0irA90BaCUcX13PiEY'
    userId=853
    fromw=2
    businessType=0
    mwAuthToken='oU1GzwjVSuSW0py2jhJY-B9owbslwB9nSgWO1yyjUOYUEj64kdNBbpMIz6beuR8sjW3uPS7EdGU0bsTEXDkiubfunR1HR9hsoFgrDEhipJE3k-Z'
    tableNo='001'       #桌名
    tableId='001'       #桌号
    shopUrl = "http://qr-api.uat.9now.net/pay/api/shop.detail"      #获取店铺信息
    orderUrl = "http://qr-st.api.9now.net/pay/api/order.detail"        #获取订单信息
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
        shopUrl = "http://qr-st.mwee.9now.net/pay/api/shop.detail"
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
                     'shopName': self.shopName, 'thirdAccess': self.thirdAccess, 'openid': self.openId,'userid':self.userId,
                     'businessType':self.businessType,'fromw':self.fromw,'mwAuthToken':self.mwAuthToken}
        try:
            orderInform = requests.post(self.orderUrl, data=orderData, headers=self.headers)
            
            orderInform.status_code
        except:
            print("无法请求订单信息失败")
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
    def get_dict_value(self,keyName, dictName):
        for key, val in dictName.items():
            if (key == keyName):
                return val
            else:
                if (isinstance(val, dict)):
                    self.get_dict_value(keyName,val)
        return


class GetOrder(unittest.TestCase,testShop):
    #普通菜拉单、5折扣菜拉单、特价菜拉单
    def test_normal_dishes(self):
        tableId = '001'
        tableNo = '001'
        orderInfo = self.get_order(tableId, tableNo)
        try:
            if(isinstance(orderInfo,dict)):
                data=orderInfo.get('data')
                #self.asserNotEqual(data,'12')
                if(isinstance(data,dict)):
                    dishs=data.get('goods','该健不存在')
                    try:
                        print(dishs)
                    except:
                        print()
            else:
                print(orderInfo)
        except:
            print("get dishes error")
        pass

    def test_set_meal(self):
        pass

    pass

class MakeOrder(unittest.TestCase,testShop):
    pass

class PayOrder(unittest.TestCase,testShop):
    pass
