#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 19:16:04
# @File           : crud.py
# @IDE            : PyCharm
# @desc           :
from core.crud import DalBase
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas


class BoardDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(BoardDal, self).__init__()
        self.db = db
        self.model = models.QuantBoard
        self.schema = schemas.BoardSimpleOut
