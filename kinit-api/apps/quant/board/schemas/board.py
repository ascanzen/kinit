#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/01/31 19:54
# @File           : board.py
# @IDE            : PyCharm
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class Board(BaseModel):
    rank: int | None = Field(None, title="排名")
    board_name: str | None = Field(None, title="板块名称")
    board_code: str | None = Field(None, title="板块代码")
    latest_price: float | None = Field(None, title="最新价")
    change_amount: float | None = Field(None, title="涨跌额")
    change_percent: float | None = Field(None, title="涨跌幅")
    market_cap: float | None = Field(None, title="总市值")
    turnover_rate: float | None = Field(None, title="换手率")
    rising_count: int | None = Field(None, title="上涨家数")
    falling_count: int | None = Field(None, title="下跌家数")
    leading_stock: str | None = Field(None, title="领涨股票")
    leading_stock_change_percent: float | None = Field(None, title="领涨股票-涨跌幅")


class BoardSimpleOut(Board):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_datetime: DatetimeStr = Field(..., title="创建时间")
    update_datetime: DatetimeStr = Field(..., title="更新时间")
