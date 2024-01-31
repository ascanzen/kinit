#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 15:34:45
# @File           : __init__.py
# @IDE            : PyCharm
# @desc           : 初始化文件


from db.db_base import BaseModel
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Float, Integer


class QuantStock(BaseModel):
    __tablename__ = "quant_stock"
    __table_args__ = ({'comment': '股票表'})

    code: Mapped[str] = mapped_column(String(10), comment="代码")
    title: Mapped[str] = mapped_column(String(50), comment="名称")
    latest_price: Mapped[float] = mapped_column(Float, comment="最新价")
    change_percent: Mapped[float] = mapped_column(Float, comment="涨跌幅")
    change_amount: Mapped[float] = mapped_column(Float, comment="涨跌额")
    volume: Mapped[int] = mapped_column(Integer, comment="成交量")
    turnover: Mapped[float] = mapped_column(Float, comment="成交额")
    amplitude: Mapped[float] = mapped_column(Float, comment="振幅")
    highest: Mapped[float] = mapped_column(Float, comment="最高")
    lowest: Mapped[float] = mapped_column(Float, comment="最低")
    today_open: Mapped[float] = mapped_column(Float, comment="今开")
    yesterday_close: Mapped[float] = mapped_column(Float, comment="昨收")
    volume_ratio: Mapped[float] = mapped_column(Float, comment="量比")
    turnover_rate: Mapped[float] = mapped_column(Float, comment="换手率")
    pe_ratio: Mapped[float] = mapped_column(Float, comment="市盈率-动态")
    pb_ratio: Mapped[float] = mapped_column(Float, comment="市净率")
    total_market_value: Mapped[float] = mapped_column(Float, comment="总市值")
    circulating_market_value: Mapped[float] = mapped_column(Float, comment="流通市值")
    rise_speed: Mapped[float] = mapped_column(Float, comment="涨速")
    five_minute_change: Mapped[float] = mapped_column(Float, comment="5分钟涨跌")
    sixty_day_change_percent: Mapped[float] = mapped_column(Float, comment="60日涨跌幅")
    year_to_date_change_percent: Mapped[float] = mapped_column(Float, comment="年初至今涨跌幅")
