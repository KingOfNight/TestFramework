import testcase
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
