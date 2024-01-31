#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 20:33:19
# @File           : views.py
# @IDE            : PyCharm
# @desc           :


from fastapi import APIRouter, Depends
from utils.response import SuccessResponse
from . import schemas, crud, models

app = APIRouter()


