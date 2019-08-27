# -*- coding: utf-8 -*-
"""
Created on 2019/8/26

@author: susmote
"""
from Func import Utils
import datetime


if __name__ == '__main__':
    judge = True
    pay_days = 0
    now_day = datetime.datetime.now()
    while judge:
        try:
            pay_days = int(input("Please enter the numbers of days you want to pay this month: "))
            judge = False
        except Exception:
            print("Your input is incorrect,please re-enter!")
    day_list = Utils.rand_days_of_month(pay_days)
    month_credits = 0
    for i in range(len(day_list)):
        credits_today, alipay_credits,tenpay_credits = Utils.rand_credits_alipay_tenpay(350, 600)
        month_credits += credits_today
        if now_day.day == day_list[i]:
            print("\033[31m%s月%2s日: Total:%s,  alipay:%s, tenpay:%s" % (now_day.month, day_list[i], credits_today, alipay_credits, tenpay_credits))
        else:
            print("\033[37m%s月%2s日: Total:%s,  alipay:%s, tenpay:%s"%(now_day.month,day_list[i], credits_today,alipay_credits, tenpay_credits))

    print("\033[34m%s月你一共使用了%s额度，共获得%s积分"%(now_day.month, month_credits, month_credits*5))
    print("\033[0m")