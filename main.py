# -*- coding: utf-8 -*-
"""
Created on 2019/8/26

@author: susmote
"""
from Func import Utils


if __name__ == '__main__':
    judge = True
    while judge:
        try:
            pay_days = int(input("Please enter the numbers of days you want to pay this month: "))
            judge = False
        except Exception:
            print("Your input is incorrect,please re-enter!")
    day_list = Utils.rand_days_of_month(pay_days)