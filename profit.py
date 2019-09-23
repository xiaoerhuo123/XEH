#!/usr/bin/env python
# encoding: utf-8

"""
@author: XEH
@software: PyCharm
@time: 9/23/19 19：25
@description：分析所得到的利润
"""
import xlrd
import  math
import pandas as pd
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def main():
    data = xlrd.open_workbook('D:\\pycharm\\projects\\class\\danguanshuju\\单关.xlsx')
    sheet = data.sheet_by_index(0)
    list0 = (sheet.col_values(0))  #比赛日期
    list2 = (sheet.col_values(2))  #全场比分
    Goals_in_list = [0] * len(list0)
    result = []
    n = 0
    for i in range(1,len(list0)):
        Score_List = list2[i]
        Host_Goals = eval(Score_List[0])
        Guest_Goals = eval(Score_List[2])
        Total_Goals = Host_Goals + Guest_Goals
        if Total_Goals <= 3:
            Goals_in_list[i-1] = 1
        else:
            Goals_in_list[i-1] = 0
    List = Goals_in_list[::-1][1:]
    money = int(input("Please input money : "))
    for j in List:
        if j == 0:
            n += 1
            result.append(n)
        elif j != 0:
            result.append(n + 1)
            n = 0
    a = List.count(0)
    b = List.count(1)
    profit = (b * money * 1.8) - (money * (a + b)) # 一般狗万的小于3球的赔率在
    print(a)
    print(b)
    print(profit)
if __name__ == '__main__':
    main()