"""
PyEconomy
=========

Economy bot for entertainment

(Based on discord UnbelievaBoat)


Functions user:

-work (in maintenance)

-dep {cantity}

-collect (adds the money to the bank)

Functions developer:

-set currency symbol

-set a range for money to get after use the work command

"""

from datetime import datetime
import random #for the roulete
from time import sleep
from tkinter import messagebox as mgbx
from termcolor import colored
import os

clear_terminal = lambda: os.system('cls')

HOUR = int(datetime.now().strftime("%H"))


pocket_money = 0
bank_money = 0
total_money = pocket_money+bank_money

roulete={
"red":60,
"red 2":70,
"red 3":30,
"red 4":40,
"red 5":20,
"black":90,
"black 2":50,
"black 3":80,
"black 4":100,
"white":10,
}

class functions_economy():
    
    def set_currency(self, currency_symbol:str):
        
        self.currency = currency_symbol
        return self.currency
    
    
    def _set_work(self, range_money=(0, 0), phrase=""):
        self.phrase = phrase
        self.range = range_money
        
    def save_money(self, money:int):
        """
        :parameter string: return the money as str
        """
        
        self.cantity = money
        self.first_ = self.cantity+bank_money
        self.second_ = self.cantity-pocket_money
        self.third_ = (self.first_, self.second_)
        self.third_as_str = str(self.third_)
        
        with open(file="user/money", mode="w", encoding="utf-8") as money_file:
            write = money_file.write(self.third_as_str)
    
    def set_item_shop(self, item:str, price:int):
        self.item = item
        self.price = price
        self.price_str = str(price)
        self.all = self.item + self.price_str + "\n"
        with open(file="developer/shop", mode="w", encoding="utf-8") as shop_file:
            shop_file.write(self.all)
    
    def set_collect(self, role, money_income:int, delay=12):
        
        """
        For developers:
        
        Set the delay time in 24hs format
        """
        
        self.income_sum = money_income+bank_money
        self.income_sum_str = str(self.income_sum)
        self.delay = delay #wait to the hour setted for collect
        self.role_user_income = role
    
    def work(self):
        #in maintenance
        for i in range(self.range[0], self.range[1]):
            self.work_ = self.phrase + str(i) + self.currency 
            #example: "you worked and u've get 100$"
            self.add_money = i + pocket_money #add the number from the range to the pocket_money
            self.add_money #summon the function
    
    def _set_roulete(self, maximun_money_win:int, wait_time:int):
        self.wait = wait_time
        self.maximum_money = maximun_money_win
        return self.maximum_money
    
    #Economy games
    
    def roulete(self, place="", bet=100):
        self.place = place
        self.bet = bet
        self.get_place = random.randint(0, 100)
        
        with open(file="user/money", mode="w", encoding="utf-8") as money_file:
            
            add_money = pocket_money + bet
            delete_money = pocket_money - bet
            write_money = money_file.write
            str_delete_money = str(delete_money)
            str_add_money = str(add_money)
            add_pocket_to_bank = pocket_money+bank_money
            str_add_pocket_to_bank = str(add_pocket_to_bank)
        
        with open(file="user/money", encoding="utf-8") as money_user:
            
            read_money = money_user.read()
        
        if pocket_money < 100 & self.bet < 100: 
            #if the pocket money & the bet is lower than 100, do nothing
            mgbx.showerror(title="error with roulete",message="you most have 100 in your pocket & set minimum 100 of money to play roulete")
            
        if pocket_money > 100 & self.bet < 100:
            mgbx.showerror(title="error with roulete",message="you most set minimum 100 of money to play roulete")
        
        if pocket_money > 100 & self.bet > 100:
            #if the pocket money is higher than 100 and the bet too
            
            #roulete red
            
            if self.place == "red" & self.get_place >= roulete["red"]:
                add_money
                write_money(str_add_money)
            
            elif self.place == "red" & self.get_place <= roulete["red"]:
                delete_money
                write_money(str_delete_money)
            
            elif self.place == "red" & self.get_place != roulete["red"]:
                add_pocket_to_bank
                write_money(str_add_pocket_to_bank)

            #roulete red 2
            
            if self.place == "red 2" & self.get_place >= roulete["red 2"]:
                add_money
                write_money(str_add_money)
            
            elif self.place == "red 2" & self.get_place <= roulete["red 2"]:
                delete_money
                write_money(str_delete_money)
            
            elif self.place == "red 2" & self.get_place != roulete["red 2"]:
                add_pocket_to_bank
                write_money(str_add_pocket_to_bank)

            #roulete red 3
            
            if self.place == "red 3" & self.get_place >= roulete["red 3"]:
                add_money
                write_money(str_add_money)
            
            elif self.place == "red 3" & self.get_place <= roulete["red 3"]:
                delete_money
                write_money(str_delete_money)
            
            elif self.place == "red 3" & self.get_place != roulete["red 3"]:
                add_pocket_to_bank
                write_money(str_add_pocket_to_bank)

            #roulete red 4
            
            if self.place == "red 4" & self.get_place >= roulete["red 4"]:
                add_money
                write_money(str_add_money)
            
            elif self.place == "red 2" & self.get_place <= roulete["red 4"]:
                delete_money
                write_money(str_delete_money)
            
            elif self.place == "red 2" & self.get_place != roulete["red 4"]:
                add_pocket_to_bank
                write_money(str_add_pocket_to_bank)

            #roulete red 5
            
            if self.place == "red 2" & self.get_place >= roulete["red 5"]:
                add_money
                write_money(str_add_money)
            
            elif self.place == "red 2" & self.get_place <= roulete["red 5"]:
                delete_money
                write_money(str_delete_money)
            
            elif self.place == "red 2" & self.get_place != roulete["red 5"]:
                add_pocket_to_bank
                write_money(str_add_pocket_to_bank)

            #roulete black
            
            if self.place == "black" & self.get_place >= roulete["black"]:
                add_money
                write_money(str_add_money)
            
            elif self.place == "black" & self.get_place <= roulete["black"]:
                delete_money
                write_money(str_delete_money)
            
            elif self.place == "black" & self.get_place != roulete["black"]:
                add_pocket_to_bank
                write_money(str_add_pocket_to_bank)
    
    def _set_guess_number(self, maximum_won:int):
        self.max_won = maximum_won
        return self.max_won
    
    def guess_number(self, number:int):
        
        self.random_number = random.randint(0, 10)
        self.number = number
        
        with open(file="user/money", mode="w", encoding="utf-8") as money_file:
            won = self.max_won + pocket_money
            lost = self.max_won - pocket_money
            won_str = f"{won}"
            lost_str = f"{lost}"
            
            if won:
                money_file.write(f"{won}")
            elif lost:
                money_file.write(f"{lost}")
        
        #number 1
        
        if self.number & self.random_number == 1:
            won
            print(f"u won {won}")
        
        elif self.number == 1  & self.random_number < 1:
            lost
            print(f"u lost {lost}")
        
        elif self.number == 1 & self.random_number > 1:
            lost
            print(f"u lost {lost}")
            
        elif self.number == 2 & self.random_number == 1:
            lost
            print(f"u lost {lost}")
            
        #number 2
        
        elif self.number & self.random_number == 2:
            won
            print(f"u won {won}")

        elif self.number == 2 & self.random_number != 2:
            lost
            print(f"u lost {lost}")
        
        elif self.number == 2 & self.random_number > 2:
            lost
            print(f"u lost {lost}")
            
        #number 3
        
        if self.number == 3 & self.random_number == 3:
            won
            print(f"u won {won}")
            
        elif self.number == 3 & self.random_number !=3:
            lost
            print(f"u lost {lost}")
            
        elif self.number == 3 & self.random_number < 3:
            lost
            print(f"u lost {lost}")
            
        #number 4

        if self.number & self.random_number == 4:
            won
            print(f"u won {won}")
            
        elif self.number == 4 & self.random_number !=4:
            lost
            print(f"u lost {lost}")
        
        elif self.number == 4 & self.random_number < 4:
            lost
            print(f"u lost {lost}")
            
    def collect(self):
        
        with open(file="user/money", mode="w", encoding="utf-8") as money_file:
            
            with open(file="user/roles", encoding="utf-8") as role_user:
                user_roles = role_user.read()
            
            with open(file="user/audit", mode="w", encoding="utf-8") as audit_log:
                write_audit_log = audit_log.write
                audit_log_collect = f"collect at: {HOUR}" + "\n" #Hour at the user did the collect
                
            if HOUR >= self.delay & self.role_user_income in user_roles:
                money_file.write(self.income_sum_str)
                write_audit_log(audit_log_collect)
            else:
                None
            
if __name__ == "__main__":
    
    clear_terminal()
    print(colored("Greatings from Ecobot :)\nPridely made in mexico", "green"))