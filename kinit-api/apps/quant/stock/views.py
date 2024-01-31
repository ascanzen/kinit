#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 16:27:00
# @File           : views.py
# @IDE            : PyCharm
# @desc           :
from apps.vadmin.auth.utils.current import AllUserAuth
from core.dependencies import IdList
from . import models, schemas, params, crud
from core.database import db_getter
from sqlalchemy.ext.asyncio import AsyncSession
from apps.vadmin.auth.utils.validation.auth import Auth
from fastapi import APIRouter, Depends
from utils.response import SuccessResponse



app = APIRouter()





###########################################################
#    股票
###########################################################
@app.get("/stock", summary="获取股票列表", tags=["股票"])
async def get_stock_list(p: params.StockParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.StockDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    return SuccessResponse(datas, count=count)


@app.post("/stock", summary="创建股票", tags=["股票"])
async def create_stock(data: schemas.Stock, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.StockDal(auth.db).create_data(data=data))


@app.delete("/stock", summary="删除股票", description="硬删除", tags=["股票"])
async def delete_stock_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.StockDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/stock/{data_id}", summary="更新股票", tags=["股票"])
async def put_stock(data_id: int, data: schemas.Stock, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.StockDal(auth.db).put_data(data_id, data))


@app.get("/stock/{data_id}", summary="获取股票信息", tags=["股票"])
async def get_stock(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.StockSimpleOut
    return SuccessResponse(await crud.StockDal(db).get_data(data_id, v_schema=schema))

