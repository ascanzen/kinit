#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/01/31 19:54
# @File           : board.py
# @IDE            : PyCharm
# @desc           : 版块

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class BoardParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
