#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 20:33:19
# @File           : __init__.py
# @IDE            : PyCharm
# @desc           : 初始化文件

from db.db_base import BaseModel
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Float, Integer


class QuantSignal(BaseModel):
    __tablename__ = "quant_signal"
    __table_args__ = ({'comment': '信号表'})

    rank: Mapped[int] = Column(Integer, comment="排名")
    # 股票代码
    code: Mapped[str] = Column(String(10), comment="代码")
    # 策略名称
    strategy_name: Mapped[str] = Column(String(50), comment="策略名称")
    # 策略参数
    strategy_params: Mapped[str] = Column(String(50), comment="策略参数")

    signal_name: Mapped[str] = Column(String(50), comment="信号名称")
    signal_code: Mapped[str] = Column(String(10), comment="信号代码")

    # 多空方向
    direction: Mapped[str] = Column(String(10), comment="多空方向")
    # 买卖价格
    price: Mapped[float] = Column(Float, comment="买卖价格")
    # 买卖数量
    quantity: Mapped[int] = Column(Integer, comment="买卖数量")
    # 买卖金额
    amount: Mapped[float] = Column(Float, comment="买卖金额")
    # 买卖时间
    time: Mapped[str] = Column(String(50), comment="买卖时间")
