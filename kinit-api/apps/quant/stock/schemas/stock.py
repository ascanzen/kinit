#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/01/31 16:28
# @File           : stock.py
# @IDE            : PyCharm
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class Stock(BaseModel):
    code: str = Field(..., title="代码")
    title: str = Field(..., title="名称")
    latest_price: float = Field(..., title="最新价")
    change_percent: float = Field(..., title="涨跌幅")
    change_amount: float = Field(..., title="涨跌额")
    volume: int = Field(..., title="成交量")
    turnover: float = Field(..., title="成交额")
    amplitude: float = Field(..., title="振幅")
    highest: float = Field(..., title="最高")
    lowest: float = Field(..., title="最低")
    today_open: float = Field(..., title="今开")
    yesterday_close: float = Field(..., title="昨收")
    volume_ratio: float = Field(..., title="量比")
    turnover_rate: float = Field(..., title="换手率")
    pe_ratio: float = Field(..., title="市盈率-动态")
    pb_ratio: float = Field(..., title="市净率")
    total_market_value: float = Field(..., title="总市值")
    circulating_market_value: float = Field(..., title="流通市值")
    rise_speed: float = Field(..., title="涨速")
    five_minute_change: float = Field(..., title="5分钟涨跌")
    sixty_day_change_percent: float = Field(..., title="60日涨跌幅")
    year_to_date_change_percent: float = Field(..., title="年初至今涨跌幅")


class StockSimpleOut(Stock):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_datetime: DatetimeStr = Field(..., title="创建时间")
    update_datetime: DatetimeStr = Field(..., title="更新时间")
