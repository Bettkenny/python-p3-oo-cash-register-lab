#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0): 
        self.total =0
        self.discount=discount
        self.items = []
    def add_item(self, title, price, quatity=1):
        self.total += price * quatity
        self.items.extend([title] *quatity)
    def substract_last_item(self):
         if self.items:
             last_item = self.items.pop()
             self.total -= last_item  
    def apply_discount(self):
        if self.discount > 0:
          self.total -=self.total * (self.discount / 100)
          print("After the discount, the total comes to $800.")
        else:
          print("There is no discount to apply.")
    def get_item_price(self, item):
        price= {
           "apple":0.99,
           "tomato":1.76,
        }
        return price.get(item, 0)
    def void_last_transaction(self, ):
        if self.items:
           last_item= self.item[-1]
           last_item_price = self.get_item_price(last_item)
           occurrences = self.items.count(last_item)
           self.items = self.items[:-occurrences]
           self.total -=(last_item_price *occurrences)
           if not self.items:
              self.total = 0.0

    
        pass
