# -*- coding: utf-8 -*-
"""
Created on 2019/8/26 

@author: LoyeLee
"""
import calendar
import datetime
import random


def rand_days_of_month(days):
    """
    get rand days of the month
    :param days: days
    :return: list rand days
    """
    now_day = datetime.datetime.now()
    month_days = calendar.monthrange(now_day.year, now_day.month)[1]
    day_list = [i for i in range(1, month_days + 1)]
    if days > month_days:
        print("Your input num has big than the Max of the month,Please rewrite")
        exit(0)
    else:
        if days == month_days:
            print(day_list)
        else:
            day_list = random.sample(day_list, days)
            day_list.sort()
    return day_list


def rand_credits_alipay_tenpay(min_credits, max_credits):
    """
    random to produce the alipay and tenpay nums
    :param min_fund: the minimum credits of this day
    :param max_fund: the maximum credits of this day
    :return:alipay and tenpay credits
    """
    credits_today = random.randint(min_credits, max_credits)
    alipay_credits = random.randint(int(min_credits/2), int(2*credits_today/3))
    tenpay_credits = credits_today - alipay_credits
    credits_wrap = []
    return credits_today, alipay_credits, tenpay_credits


def get_min_max_credits(day_count, max_credits_month):
    """
    get the max and min credits with total avg
    :param day_count: days of the month
    :param max_credits_month: the maximum credits
    :return: max_credits and min credits
    """
    avg_credit = max_credits_month / day_count
    max_credits = (3*avg_credit)/2
    min_credits = avg_credit/2
    return int(min_credits), int(max_credits)