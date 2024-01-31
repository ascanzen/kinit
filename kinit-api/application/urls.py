# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2021/10/19 15:47
# @File           : urls.py
# @IDE            : PyCharm
# @desc           : 路由文件

from apps.vadmin.auth.utils.login import app as auth_app
from apps.vadmin.auth.views import app as vadmin_auth_app
from apps.vadmin.system.views import app as vadmin_system_app
from apps.vadmin.record.views import app as vadmin_record_app
from apps.vadmin.workplace.views import app as vadmin_workplace_app
from apps.vadmin.analysis.views import app as vadmin_analysis_app
from apps.vadmin.help.views import app as vadmin_help_app
from apps.vadmin.resource.views import app as vadmin_resource_app
from apps.quant.stock.views import app as quant_stock_app


# 引入应用中的路由
urlpatterns = [
    {"ApiRouter": auth_app, "prefix": "/auth", "tags": ["系统认证"]},
    {"ApiRouter": vadmin_auth_app, "prefix": "/vadmin/auth", "tags": ["权限管理"]},
    {"ApiRouter": vadmin_system_app, "prefix": "/vadmin/system", "tags": ["系统管理"]},
    {"ApiRouter": vadmin_record_app, "prefix": "/vadmin/record", "tags": ["记录管理"]},
    {"ApiRouter": vadmin_workplace_app, "prefix": "/vadmin/workplace", "tags": ["工作区管理"]},
    {"ApiRouter": vadmin_analysis_app, "prefix": "/vadmin/analysis", "tags": ["数据分析管理"]},
    {"ApiRouter": vadmin_help_app, "prefix": "/vadmin/help", "tags": ["帮助中心管理"]},
    {"ApiRouter": vadmin_resource_app, "prefix": "/vadmin/resource", "tags": ["资源管理"]},
    # {"ApiRouter": quant_stock_app, "prefix": "/quant/stock", "tags": ["股票"]},
]

import importlib
import pkgutil
# 导入apps.quant模块的所有子模块的.model模块
class_name = "app"
quant_module = importlib.import_module('apps.quant')
for _, module_name, _ in pkgutil.iter_modules(quant_module.__path__):
    module = importlib.import_module(f'apps.quant.{module_name}.views')
    # 导入模块中的所有类
    for attr in dir(module):
        if attr.startswith('__'):
            continue
        
        if attr == class_name:
            class_obj = getattr(module, class_name)
            globals()[attr] = class_obj
            urlpatterns.append({"ApiRouter": class_obj, "prefix": f"/quant/{module_name}", "tags": None})

            
