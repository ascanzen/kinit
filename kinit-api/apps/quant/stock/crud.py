#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 16:27:00
# @File           : crud.py
# @IDE            : PyCharm
# @desc           :
from . import models, schemas
from core.crud import DalBase
from sqlalchemy.ext.asyncio import AsyncSession


class StockDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(StockDal, self).__init__()
        self.db = db
        self.model = models.QuantStock
        self.schema = schemas.StockSimpleOut
