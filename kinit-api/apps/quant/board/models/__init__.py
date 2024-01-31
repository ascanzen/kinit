#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 19:16:04
# @File           : __init__.py
# @IDE            : PyCharm
# @desc           : 初始化文件

from db.db_base import BaseModel
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Float, Integer


class QuantBoard(BaseModel):
    __tablename__ = "quant_board"
    __table_args__ = ({'comment': '板块表'})

    rank: Mapped[int] = Column(Integer, comment="排名")
    board_name: Mapped[str] = Column(String(50), comment="板块名称")
    board_code: Mapped[str] = Column(String(10), comment="板块代码")
    latest_price: Mapped[float] = Column(Float, comment="最新价")
    change_amount: Mapped[float] = Column(Float, comment="涨跌额")
    change_percent: Mapped[float] = Column(Float, comment="涨跌幅")
    market_cap: Mapped[float] = Column(Float, comment="总市值")
    turnover_rate: Mapped[float] = Column(Float, comment="换手率")
    rising_count: Mapped[int] = Column(Integer, comment="上涨家数")
    falling_count: Mapped[int] = Column(Integer, comment="下跌家数")
    leading_stock: Mapped[str] = Column(String(50), comment="领涨股票")
    leading_stock_change_percent: Mapped[float] = Column(Float, comment="领涨股票-涨跌幅")
