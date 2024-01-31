#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/01/31 16:28
# @File           : stock.py
# @IDE            : PyCharm
# @desc           : 股票

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class StockParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
