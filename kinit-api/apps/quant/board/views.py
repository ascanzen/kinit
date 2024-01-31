#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-01-31 19:16:04
# @File           : views.py
# @IDE            : PyCharm
# @desc           :
from utils.response import SuccessResponse
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import IdList
from apps.vadmin.auth.utils.current import AllUserAuth
from . import crud, models, params, schemas
from core.database import db_getter
from fastapi import Depends, APIRouter
from apps.vadmin.auth.utils.validation.auth import Auth



app = APIRouter()





###########################################################
#    版块
###########################################################
@app.get("/board", summary="获取版块列表", tags=["版块"])
async def get_board_list(p: params.BoardParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.BoardDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    return SuccessResponse(datas, count=count)


@app.post("/board", summary="创建版块", tags=["版块"])
async def create_board(data: schemas.Board, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.BoardDal(auth.db).create_data(data=data))


@app.delete("/board", summary="删除版块", description="硬删除", tags=["版块"])
async def delete_board_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.BoardDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/board/{data_id}", summary="更新版块", tags=["版块"])
async def put_board(data_id: int, data: schemas.Board, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.BoardDal(auth.db).put_data(data_id, data))


@app.get("/board/{data_id}", summary="获取版块信息", tags=["版块"])
async def get_board(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.BoardSimpleOut
    return SuccessResponse(await crud.BoardDal(db).get_data(data_id, v_schema=schema))

