#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:12:34 2022

@author: shawn
"""

#%%
# Parent class: User
# stores details of name, age, gendr
# Has a function to show user details
# Child class: Bank
# stores details of account balance; amount
# allows for deposit, withdraw, check balance

#%%
# Parent Class
customer_dic = {}

class User():
    def __init__(self, name, age, gender):
        self.name   = name
        self.age    = age
        self.gender = gender
    
    def show_details(self):
        print("User detilas")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        
        if self.name not in customer_dic.keys():
            customer_dic.update({self.name: [self.age, self.gender]})

# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance updated: ", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance available: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ", self.balance)
    
    def check_balance(self):
        self.show_details()
        print("Account balance: ", self.balance)
#%%