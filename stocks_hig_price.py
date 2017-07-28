#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tushare as ts
import datetime

stock_info=ts.get_stock_basics()

def all_stocks():
    for stock_id in stock_info.index:
        if break_high(stock_id,60):
            print 'High price on'
            print stock_id,
            print stock_info.ix[stock_id]['name'].decode('utf-8')

def break_high(stock_id,days):
    end_day=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
    days=days*7/5
    start_day=end_day-datetime.timedelta(days)
    start_day=start_day.strftime("%Y-%m-%d")
    end_day=end_day.strftime("%Y-%m-%d")
    df=ts.get_h_data(stock_id,start=start_day,end=end_day)
    period_high=df['high'].max()
    today_high=df.iloc[0]['high']
    if today_high>=period_high:
        return True
    else:
        return False

all_stocks()