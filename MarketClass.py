class Market:
    def __init__(self,name,store_hours,employees,total_money):
        self.name = name
        self.store_hours = store_hours
        self.employees = employees
        self.total_money = total_money
        self.bag = {}

    def buy(self,item,price):
        self.bag[item] = price
        print(self.bag)
        self.total_money = self.total_money - price
        print (self.total_money)

    def returning(self,item):
        if item in self.bag:
            self.total_money = self.total_money + self.bag[item]
            del self.bag[item]
            print (self.bag)
            print (self.total_money)
        else:
            print ("No item")
